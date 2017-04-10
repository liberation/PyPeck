from pypeck.scrapper import Scrapper


class PyPeck(object):
    def __init__(self, url, config):
        self.url = url
        self.config = config
        self.scrapper = Scrapper.get_scrapper_for_url(url, config)

    def process(self):
        self.scrapper.extract_metas()

    def get_datas(self):
        return self.scrapper.get_datas()

