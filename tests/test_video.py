import unittest
from pypeck.scrapper import Scrapper
from pypeck.scrapper.video import VideoScrapper


class VideoScrapperTest(unittest.TestCase):

    def test_scrap_content(self):
        scrapper = Scrapper.get_scrapper_for_url(
            'https://www.youtube.com/watch?v=igpa6DXMTCA',
        )
        self.assertIs(scrapper.__class__, VideoScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()
        self.assertEqual(datas.get('aspect_ratio'), 0.5625)
        self.assertEqual(datas.get('provider'), 'YouTube')


        scrapper = Scrapper.get_scrapper_for_url(
            'https://vimeo.com/205021741',
        )
        self.assertIs(scrapper.__class__, VideoScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()
        self.assertEqual(datas.get('aspect_ratio'), 0.75)
        self.assertEqual(datas.get('provider'), 'Vimeo')
        self.assertEqual(
            datas.keys(),
            ['url', 'aspect_ratio', 'thumbnail_url', 'video_url', 'provider']
        )

        scrapper = Scrapper.get_scrapper_for_url(
            'http://www.dailymotion.com/video/x5ftqxm_juliette-meadel-'
            'sur-les-lyceens-francais-blesses-a-londres-leur-vie-n-'
            'est-pas-en-danger_news'
        )

        scrapper.extract_metas()

        datas=scrapper.get_datas()
        self.assertEqual(datas.get('aspect_ratio'), 0.5625)
        self.assertEqual(datas.get('provider'), 'Dailymotion')
        self.assertEqual(
            datas.keys(),
            ['url', 'aspect_ratio', 'thumbnail_url', 'video_url', 'provider']
        )
