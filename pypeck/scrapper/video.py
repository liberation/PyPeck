import re

from pypeck.scrapper import Scrapper
from pypeck.scrapper.constants import ASSET_TYPES


class VideoScrapper(Scrapper):

    type = ASSET_TYPES.video

    DEFAULT_ASPECT_RATIO = 0.5625

    dom_matches = [
        ('meta', {'name': 'og:type', 'content': re.compile(r'^video$'), }),
        ('meta', {'property': 'og:type', 'content': re.compile(r'^video$'), }),

        ('meta', {'name': 'og:video', 'content': re.compile(r'^https?://'), }),
        ('meta', {'property': 'og:video',
                  'content': re.compile(r'^https?://'), }),

        ('meta', {'name': 'og:video_secure_url',
                  'content': re.compile(r'^https://'), }),
        ('meta', {'property': 'og:video_secure_url',
                  'content': re.compile(r'^https://'), }),
    ]

    def get_url(self):
        if self.dom.findAll('link', attrs={'rel': 'canonical'}):
            return self.dom.findAll('link',
                                    attrs={'rel': 'canonical'})[0]['href']
        else:
            return self.url

    def extract_provider_content(self):
        pass

    def get_thumbnail_url(self):
        return self.get_meta_from_list(['og:image:secure_url', 'og:image'])

    def get_video_url(self):
        return self.get_meta_from_list(
            ['twitter:player', 'og:video:secure_url', 'og:video:url']
        )

    def get_aspect_ratio(self):
        width = self.get_meta_from_list(
            ['og:video:width', 'twitter:player:width']
        )
        height = self.get_meta_from_list(
            ['og:video:height', 'twitter:player:height']
        )
        try:
            return float(height)/float(width)
        except TypeError:
            return self.DEFAULT_ASPECT_RATIO

    def get_datas(self):
        return {
            'thumbnail_url': self.get_thumbnail_url(),
            'url': self.get_url(),
            'video_url': self.get_video_url(),
            'provider': self.get_provider(),
            'aspect_ratio': self.get_aspect_ratio(),
        }
