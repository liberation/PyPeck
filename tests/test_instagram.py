# -*- coding: utf-8 -*-
import unittest
from datetime import datetime
from pypeck.scrapper import Scrapper
from pypeck.scrapper.instagram import InstagramScrapper


class InstagramScrapperTest(unittest.TestCase):

    def test_scrap_content(self):
        scrapper = Scrapper.get_scrapper_for_url(
            'https://www.instagram.com/p/BRIsag5ljtJ/',
        )
        self.assertIs(scrapper.__class__, InstagramScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()
        self.assertEqual(
            datas.keys(),
            ['caption', 'video', 'url', 'provider', 'date', 'image', 'id',
             'user']
        )

        self.assertIsNone(datas.get('video'))
        self.assertIsNotNone(datas.get('image'))
        self.assertEqual('1488454318', datas.get('date').strftime('%s'))

        scrapper = Scrapper.get_scrapper_for_url(
            'https://www.instagram.com/p/BReuIYBl9P5/'
            '?taken-by=slackline_pro&hl=fr'
        )
        self.assertIs(scrapper.__class__, InstagramScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()

        self.assertEqual(
            datas.keys(),
            ['caption', 'video', 'url', 'provider', 'date', 'image', 'id',
             'user']
        )
        self.assertIsNotNone(datas.get('video'))
        self.assertEqual('1489193416', datas.get('date').strftime('%s'))
