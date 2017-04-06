# -*- coding: utf-8 -*-
import unittest
import os
from datetime import datetime
from pypeck.scrapper import Scrapper
from pypeck.scrapper.facebook import FacebookScrapper


class FacebookScrapperTest(unittest.TestCase):
    def setUp(self):
        self.config = {
            'facebook': {
                'TOKEN':
                    os.environ.get('FB_TOKEN'),
            },
        }

    def test_scrap_content(self):
        scrapper = Scrapper.get_scrapper_for_url(
            'https://www.facebook.com/Liberation/posts/10155040633377394',
            self.config
        )
        self.assertIs(scrapper.__class__, FacebookScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()
        self.assertIsNotNone(datas.get('content'))
        self.assertIsNone(datas.get('video'))
        self.assertIsNotNone(datas.get('image'))
        self.assertIsInstance(datas.get('date'), datetime)
        self.assertEqual(
            datas.get('url'),
            'https://www.facebook.com/Liberation/posts/10155040633377394'
        )
        self.assertEqual(datas.get('user'), {
            'url': u'https://www.facebook.com/147126052393',
            'username': u'Libération'}
         )


        scrapper = Scrapper.get_scrapper_for_url(
            'https://www.facebook.com/BFMTV/videos/10155428810852784/',
            self.config
        )
        self.assertIs(scrapper.__class__, FacebookScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()
        self.assertIsNotNone(datas.get('content'))
        self.assertIsNotNone(datas.get('video'))
        self.assertIsNotNone(datas.get('image'))
        self.assertIsInstance(datas.get('date'), datetime)
        self.assertEqual(
            datas.get('url'),
            'https://www.facebook.com/BFMTV/videos/10155428810852784/'
        )

        scrapper = Scrapper.get_scrapper_for_url(
            'https://www.facebook.com/Liberation/videos/'
            'vb.147126052393/10155019316047394/?type=2&theater',
            self.config
        )
        self.assertIs(scrapper.__class__, FacebookScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()

        self.assertIsNotNone(datas.get('content'))
        self.assertIsNotNone(datas.get('video'))
        self.assertIsNotNone(datas.get('image'))
        self.assertIsInstance(datas.get('date'), datetime)
        self.assertEqual(
            datas.get('url'),
            'https://www.facebook.com/Liberation/videos/10155019316047394/'
        )

        scrapper = Scrapper.get_scrapper_for_url(
            'https://www.facebook.com/Liberation/photos/'
            'a.329987802393.196415.147126052393/10155085314147394/'
            '?type=3&permPage=1',
            self.config
        )
        self.assertIs(scrapper.__class__, FacebookScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()

        self.assertIsNotNone(datas.get('content'))
        self.assertIsNone(datas.get('video'))
        self.assertIsNotNone(datas.get('image'))
        self.assertIsInstance(datas.get('date'), datetime)
        self.assertEqual(
            datas.get('url'),
            'https://www.facebook.com/Liberation/photos/'
            'a.329987802393.196415.147126052393/10155085314147394/?type=3'
        )
