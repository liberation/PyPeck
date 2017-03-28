# -*- coding: utf-8 -*-
import unittest
from pypeck.scrapper import Scrapper
from pypeck.scrapper.facebook import FacebookScrapper


class FacebookScrapperTest(unittest.TestCase):
    def test_scrap_content(self):
        scrapper = Scrapper.get_scrapper_for_url(
            'https://www.facebook.com/Liberation/posts/10155040633377394',
        )
        self.assertIs(scrapper.__class__, FacebookScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()
        self.assertEqual(
            datas.keys(),
            ['url', 'content', 'image', 'id', 'user']
        )

        scrapper = Scrapper.get_scrapper_for_url(
            'https://www.facebook.com/BFMTV/videos/10155428810852784/'
        )
        self.assertIs(scrapper.__class__, FacebookScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()
        self.assertEqual(
            datas.keys(),
            ['url', 'content', 'image', 'id', 'user']
        )
