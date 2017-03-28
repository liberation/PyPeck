import re

from BeautifulSoup import BeautifulSoup

from pypeck.scrapper import Scrapper
from pypeck.scrapper.constants import ASSET_TYPES
from pypeck.datetools import parse_datetime


class InstagramScrapper(Scrapper):

    type = ASSET_TYPES.instagram

    url_schemes = [
        r"https?:\/\/[\w\.]*instagram\.com/p/[a-zA-Z0-9_-]+",
        r"https?:\/\/instagr\.am/p/[a-zA-Z0-9_-]+"
    ]

    @classmethod
    def is_site_specific(cls):
        return True

    def extract_provider_content(self):
        pass

    def get_id(self):
        try:
            return re.findall(r'p/([a-zA-Z0-9_-]+)', self.url)[0]
        except IndexError:
            raise Exception('Cannot find post id')

    def get_image(self):
        return {
            'url': self.oembed.get('thumbnail_url'),
            'aspect_ratio':
                float(self.oembed.get('thumbnail_height')) /
                float(self.oembed.get('thumbnail_width'))
        }

    def get_video(self):
        if self.get_meta_from_list(['og:type']) == "video":
            return {
                'url': self.get_meta_from_list([
                    'og:video:secure_url',
                    'og:video'
                ]),
                'aspect_ratio':
                    float(self.get_meta_from_list(['og:video:height'])) /
                    float(self.get_meta_from_list(['og:video:width']))
            }

    def get_caption(self):
        return self.oembed.get('title')

    def get_date(self):
        bs = BeautifulSoup(self.oembed.get('html'))
        time = bs.find('time')
        return parse_datetime(time['datetime'])

    def get_user(self):
        return {
            'username': self.oembed.get('author_name'),
            'url': self.oembed.get('author_url'),
        }

    def get_datas(self):
        return {
            'id': self.get_id(),
            'caption': self.get_caption(),
            'provider': self.get_provider(),
            'image': self.get_image(),
            'video': self.get_video(),
            'url': self.get_url(),
            'user': self.get_user(),
        }
