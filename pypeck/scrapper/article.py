import re

from pypeck.scrapper import Scrapper
from pypeck.scrapper.constants import ASSET_TYPES


class ArticleScrapper(Scrapper):
    dom_matches = [
        ('meta', {'name': 'og:type', 'content': 'article', }),
        ('meta', {'property': 'og:type', 'content': 'article', }),
    ]

    type = ASSET_TYPES.article

    def get_provider(self):
        provider = super(ArticleScrapper, self).get_provider()
        if not provider:
            try:
                return re.findall('^https?://[^/]+', self.url)[0]
            except IndexError:
                return
        return provider

    def get_abstract(self):
        return self.get_meta_from_list(
            ['og:description', 'dc.description', 'description']
        )

    def get_title(self):
        return self.get_meta_from_list(
            ['og:title', 'dc.title', 'title']
        )

    def extract_provider_content(self):
        pass

    def get_datas(self):
        return {
            'provider': self.get_provider(),
            'title': self.get_title(),
            'abstract': self.get_abstract(),
            'image': self.get_meta_from_list(['og:image', 'libe:image']),
        }
