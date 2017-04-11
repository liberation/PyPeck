import unittest
from pypeck.scrapper import Scrapper
from pypeck.scrapper.article import ArticleScrapper


class ArticleScrapperTest(unittest.TestCase):

    def test_scrap_content(self):
        scrapper = Scrapper.get_scrapper_for_url(
            'http://www.liberation.fr/france/2017/02/26/a-toulouse-'
            'rideau-sur-l-ecole-musulmane_1551206',
        )
        self.assertIs(scrapper.__class__, ArticleScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()
        self.assertItemsEqual(
            datas.keys(),
            ['abstract', 'title', 'image', 'provider', 'type']
        )

        scrapper = Scrapper.get_scrapper_for_url(
            'http://www.lemonde.fr/idees/article/2017/02/27/les-elements-d-'
            'un-drame-humanitaire-de-grande-ampleur-sont-reunis-en-afrique-'
            'de-l-est_5086234_3232.html',
        )
        self.assertIs(scrapper.__class__, ArticleScrapper)

        scrapper.extract_metas()

        datas = scrapper.get_datas()
        self.assertItemsEqual(
            datas.keys(),
            ['abstract', 'title', 'image', 'provider', 'type']
        )

        scrapper = Scrapper.get_scrapper_for_url(
            'http://www.independent.co.uk/news/world/politics/donald-trump-'
            'election-made-men-more-aggressive-negotiators-a7625701.html'
        )
        self.assertIs(scrapper.__class__, ArticleScrapper)

        scrapper.extract_metas()
        datas = scrapper.get_datas()
        self.assertItemsEqual(
            datas.keys(),
            ['abstract', 'title', 'image', 'provider', 'type']
        )

        scrapper = Scrapper.get_scrapper_for_url(
            'https://medium.com/@josquindebaz/'
            'lattaque-des-groupies-agricoles-76f0c43c9ad2#.jrtdo35k2'
        )
        self.assertIs(scrapper.__class__, ArticleScrapper)
        scrapper.extract_metas()
        datas = scrapper.get_datas()
        self.assertItemsEqual(
            datas.keys(),
            ['abstract', 'title', 'image', 'provider', 'type']
        )

        scrapper = Scrapper.get_scrapper_for_url(
            'http://linuxfr.org/news/rencontre-xmpp-jabber-par-jabberfr-'
            'mardi-28-mars-2017-a-19-h-a-paris'
        )
        self.assertIs(scrapper.__class__, ArticleScrapper)
        scrapper.extract_metas()
        datas = scrapper.get_datas()
        self.assertIsNone(datas.get('image'))
        self.assertItemsEqual(
            datas.keys(),
            ['abstract', 'title', 'image', 'provider', 'type']
        )
