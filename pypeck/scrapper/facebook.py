# -*- coding: utf-8 -*-
from __future__ import absolute_import

import re

from pypeck.datetools import parse_datetime
from pypeck.scrapper import Scrapper
from pypeck.scrapper.constants import ASSET_TYPES

import facebook


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

    def __init__(self, *args, **kwargs):
        super(FacebookScrapper, self).__init__(*args, **kwargs)
        self.api_data = {}

        self.API = facebook.GraphAPI(
            access_token=self.config.get('facebook', {}).get('TOKEN', None),
            version='2.7')

    def extract_metas(self):
        self.extract_og_metas()
        self.extract_provider_content()

    def get_post_id(self):
        username, post_type, u, post_id = re.findall(
            r'facebook.com/([a-zA-Z0-9\\.\\-]+)/'
            r'(posts|activity|photos|videos)/([^/]*/)?(\d{10,})',
            self.get_url())[0]

        user_id = self.API.get_object(username).get('id')
        return "{}_{}".format(user_id, post_id)

    def extract_provider_content(self):
        self.api_data = self.API.get_object(
            self.get_post_id(),
            fields='created_time,from,message,name,picture,type,source'
        )

    def get_id(self):
        return re.findall('(\d+)/?$', self.get_url())[0]

    def get_url(self):
        return self.og.get('og:url')

    def get_content(self):
        return self.api_data.get('message')

    def get_image(self):
        return self.api_data.get('picture', None)

    def get_video(self):
        return self.api_data.get('source', None)

    def get_user(self):
        return {
            'username': self.api_data.get('from').get('name'),
            'url': u'https://www.facebook.com/{}'.format(
                self.api_data.get('from').get('id')
            ),
        }

    def get_date(self):
        return parse_datetime(self.api_data.get('created_time'))

    def get_datas(self):
        return {
            'id': self.get_id(),
            'url': self.get_url(),
            'date': self.get_date(),
            'content': self.get_content(),
            'image': self.get_image(),
            'video': self.get_video(),
            'user': self.get_user(),
        }
