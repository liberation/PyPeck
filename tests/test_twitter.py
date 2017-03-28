# -*- coding: utf-8 -*-
import unittest
import os
from pypeck.scrapper import Scrapper
from pypeck.scrapper.twitter import TwitterScrapper


class TwitterScrapperTest(unittest.TestCase):
    def setUp(self):
        self.config = {
            'twitter': {
                'CONSUMER_KEY':
                    os.environ.get('CONSUMER_KEY'),
                'CONSUMER_SECRET':
                    os.environ.get('CONSUMER_SECRET')
            },
        }

    def test_scrap_content(self):
        scrapper = Scrapper.get_scrapper_for_url(
            'https://twitter.com/libe/status/838734699539349504',
            self.config
        )
        self.assertIs(scrapper.__class__, TwitterScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()
        self.assertEqual(datas.get('id'), '838734699539349504')
        self.assertEqual(datas.get('user').get('name'), u'Libération')

        self.assertEqual(
            datas.keys(),
            ['text', 'provider', 'rich_text', 'user', 'media', 'date', 'id', ]
        )
