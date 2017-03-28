import re

from pypeck.scrapper import Scrapper
from pypeck.scrapper.constants import ASSET_TYPES


class FacebookScrapper(Scrapper):

    type = ASSET_TYPES.facebook

    url_schemes = [
        "https?://(?:www|business)\\.facebook\\.com/[a-zA-Z0-9.]+/videos/.+",
        "https?://(?:www|m|business)\\.facebook\\.com/([a-zA-Z0-9\\.\\-]+)"
        "/(posts|activity)/(\\d{10,})",
        "https?://(?:www|m|business)\\.facebook\\.com/([a-zA-Z0-9\\.\\-]+)"
        "/photos/[^\\/]+/(\\d{10,})",
    ]

    @classmethod
    def is_site_specific(cls):
        return True

    def extract_provider_content(self):
        pass

    def get_id(self):
        return re.findall('(\d+)/?$', self.get_url())[0]

    def get_url(self):
        return self.og.get('og:url')

    def get_content(self):
        return self.og.get('og:description')

    def get_image(self):
        return self.og.get('og:image')

    def get_user(self):
        return {
            'username': self.oembed.get('author_name'),
            'url': self.oembed.get('author_url'),
        }

    def get_datas(self):
        return {
            'id': self.get_id(),
            'url': self.get_url(),
            'content': self.get_content(),
            'image': self.get_image(),
            'user': self.get_user(),
        }
