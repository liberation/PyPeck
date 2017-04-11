import re
import tweepy
from pypeck.scrapper import Scrapper
from pypeck.scrapper.constants import ASSET_TYPES


class TwitterScrapper(Scrapper):
    type = ASSET_TYPES.twitter

    url_schemes = [
        r'^https?:\/\/twitter\.com\/(?:\w+)\/status(?:es)?\/(\d+)'
    ]

    def __init__(self, *args, **kwargs):
        self.api = None
        self.tweet = None
        super(TwitterScrapper, self).__init__(*args, **kwargs)

    @classmethod
    def is_site_specific(cls):
        return True

    def get_api(self):
        if not self.api:
            auth = tweepy.OAuthHandler(
                self.config.get('twitter', {}).get('CONSUMER_KEY', None),
                self.config.get('twitter', {}).get('CONSUMER_SECRET', None)
            )

            self.api = tweepy.API(auth)
        return self.api

    def get_tweet_id(self):
        try:
            return re.findall(self.url_schemes[0], self.url)[0]
        except IndexError:
            raise Exception('Cannot find tweet id')

    def extract_provider_content(self):
        self.tweet = self.get_api().get_status(self.get_tweet_id(),
                                               tweet_mode="extended")

    def get_richtext(self):
        # Note: the algo is based on the fact that links can't overlap

        text = self.tweet.full_text

        entries = []

        for entry in self.tweet.entities.get('urls', []):
            linkified = u'<a target="_blank" href="{0}">{1}</a>'.format(
                entry[u'url'], entry[u'display_url'])
            entries.append({'indices': entry['indices'], 'text': linkified})

        for entry in self.tweet.entities.get('hashtags', []):
            linkified = (
                u'<a target="_blank" href="http://twitter.com/search?q={0}">'
                u'#{1}</a>'
                .format(entry[u'text'], entry[u'text'])
            )
            entries.append({'indices': entry['indices'], 'text': linkified})

        for entry in self.tweet.entities.get('user_mentions', []):
            linkified = (
                u'<a target="_blank" title="{0}" '
                u'href="http://twitter.com/{1}">@{2}</a>'
                .format(
                    entry[u'name'],
                    entry[u'screen_name'],
                    entry[u'screen_name']
                )
            )
            entries.append({'indices': entry['indices'], 'text': linkified})

        # remove the medias from the text, since they are already displayed
        for entry in self.tweet.entities.get('media', []):
            entries.append({'indices': entry['indices'], 'strip': True})

        entries.sort(key=lambda a: a['indices'][0])
        entries.reverse()
        for entry in entries:
            a = entry['indices'][0]
            b = entry['indices'][1]
            if entry.get('strip', False):
                text = text[:a] + text[b:]
            else:
                text = text[:a] + entry['text'] + text[b:]

        return text

    def get_media(self):
        if (hasattr(self.tweet, 'extended_entities')
                and self.tweet.extended_entities.get('media')):
            media = self.tweet.extended_entities.get('media')[0]
            media_type = media.get('type')

            if media_type in ['animated_gif', 'video']:
                video = media.get('video_info')

                variant = self.filter_video(video.get('variants'))
                if variant:
                    video_url = variant.get('url')
                    ratio_x, ratio_y = video.get('aspect_ratio')
                    aspect_ratio = float(ratio_y)/float(ratio_x)
                    return {
                        'video_url': video_url,
                        'aspect_ratio': aspect_ratio,
                    }

            elif media_type == 'photo':
                large_sizes = media.get('sizes').get('large')
                return {
                    'url': media.get('media_url_https'),
                    'aspect_ratio': (float(large_sizes.get('h')) /
                                     float(large_sizes.get('w')))
                }
        else:
            return None

    def filter_video(self, variants):
        better_idx = None

        for video in [variant for variant in variants
                      if variant.get('content_type') == 'video/mp4']:

            if (better_idx is None or
                    video.get('bitrate') >
                    variants[better_idx].get('bitrate')):
                better_idx = variants.index(video)

        return variants[better_idx] if better_idx is not None else None

    def get_datas(self):
        return {
            'id': str(self.get_tweet_id()),
            'date': self.tweet.created_at,
            'text': self.tweet.full_text,
            'rich_text': self.get_richtext(),
            'user': {
                "id": str(self.tweet.user.id),
                "name": self.tweet.user.name,
                "username": self.tweet.user.screen_name,
                "url": self.tweet.user.url,
                "profile_url": "https://twitter.com/{}".format(
                    self.tweet.user.screen_name),
                "avatar": self.tweet.user.profile_image_url
            },
            'media': self.get_media(),
            'provider': self.get_provider(),
        }
