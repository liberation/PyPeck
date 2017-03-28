# -*- coding: utf-8 -*-
import unittest
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
            ['url', 'image', 'caption', 'video', 'user', 'provider', 'id']
        )
        self.assertIsNone(datas.get('video'))
        self.assertIsNotNone(datas.get('image'))

        scrapper = Scrapper.get_scrapper_for_url(
            'https://www.instagram.com/p/BReuIYBl9P5/'
            '?taken-by=slackline_pro&hl=fr'
        )
        self.assertIs(scrapper.__class__, InstagramScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()
        self.assertEqual(
            datas.keys(),
            ['url', 'image', 'caption', 'video', 'user', 'provider', 'id']
        )
        self.assertIsNotNone(datas.get('video'))
