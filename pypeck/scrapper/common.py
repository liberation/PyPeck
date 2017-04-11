import re
import json
import urllib2
import logging
from urllib import urlencode
from BeautifulSoup import BeautifulSoup

from pypeck.scrapper.constants import OEMBED_ENDPOINTS

logger = logging.getLogger(__name__)


class MetaRegistry(type):
    MODULES = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        cls.MODULES[new_cls.__name__] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.MODULES)


class Scrapper(object):
    __metaclass__ = MetaRegistry

    url_schemes = []
    dom_matches = []

    config = {
        'twitter': {
            'CONSUMER_KEY': None,
            'CONSUMER_SECRET': None,
        },
    }

    def __new__(cls, *args, **kwargs):
        cls.get_datas = Scrapper.data_decorator(cls.get_datas)
        return super(Scrapper, cls).__new__(cls, *args, **kwargs)

    def __init__(self, url, dom, config=None):
        if config:
            self.config.update(config)
        self.url = url
        self.dom = dom
        self.og, self.twitter, self.oembed = {}, {}, {}

    @classmethod
    def is_site_specific(cls):
        return False

    @classmethod
    def is_able(cls, url, content):
        for scheme in cls.url_schemes:
            if re.match(scheme, url):
                return True
        for tag, attrs in cls.dom_matches:
            if content.findAll(tag, attrs=attrs):
                return True
        return False

    @classmethod
    def get_scrapper_for_url(cls, url, config=None):
        content = cls.download_content(url)
        scrapper_registry = Scrapper.get_registry()
        scrappers = []

        for name, scrapper in scrapper_registry.items():
            if scrapper.is_able(url, content):
                scrappers.append(scrapper)

        for scrapper in scrappers:
            if scrapper.is_site_specific():
                return scrapper(url, content, config)
        for scrapper in scrappers:
            if not scrapper.is_site_specific():
                return scrapper(url, content, config)

        return scrapper_registry.get('ArticleScrapper')(url, content, config)

    @classmethod
    def download_content(cls, url):
        request = urllib2.Request(url)
        request.add_header(
            'User-Agent',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'
        )
        result = urllib2.urlopen(request)
        return BeautifulSoup(result.read())

    @staticmethod
    def data_decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            data.update({
                'type': args[0].type
            })
            return data

        return wrapper

    def extract_metas(self):
        self.extract_og_metas()
        self.extract_twitter_metas()
        self.extract_oembed()
        self.extract_provider_content()

    def extract_og_metas(self):
        if self.dom:
            for attr in ['property', 'name']:
                for og_tag in self.dom.findAll(
                        'meta', attrs={attr: re.compile(r'^og:')}):
                    self.og.update({og_tag[attr]: og_tag['content']})

    def extract_twitter_metas(self):
        if self.dom:
            for tw_tag in self.dom.findAll(
                    'meta', attrs={'name': re.compile('^twitter:')}):
                if tw_tag.has_key('name') and tw_tag.has_key('content'):
                    self.twitter.update({tw_tag['name']: tw_tag['content']})

    def extract_oembed(self):
        for provider in OEMBED_ENDPOINTS:
            for template in provider.get('templates'):
                matches = re.findall(template, self.url)
                if matches:
                    request = urllib2.urlopen(
                        "%s?%s" % (provider.get('endpoint'),
                                   urlencode({'format': 'json',
                                              'url': self.url,
                                              }))
                    )
                    self.oembed = json.loads(request.read())

    def get_meta_from_list(self, meta_list):
        for attr in ['og', 'twitter']:
            meta_tuple = getattr(self, attr)
            for meta in meta_list:
                if meta in meta_tuple:
                    return meta_tuple.get(meta)
        for meta in meta_list:
            matches = self.dom.findAll('meta', attrs={'name': meta})
            if matches:
                return matches[0].get('content')
            matches = self.dom.findAll(meta)
            if matches:
                return matches[0].text

    def get_url(self):
        url = self.get_meta_from_list(['og:url', 'canonical'])
        return url if url else self.url

    def get_raw_datas(self):
        pass

    def get_provider(self):
        return self.get_meta_from_list(['og:site_name'])

    def extract_provider_content(self):
        raise NotImplementedError

    def get_datas(self):
        raise NotImplementedError
