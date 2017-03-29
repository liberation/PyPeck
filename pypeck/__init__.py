from .scrapper import Scrapper


class PyPeck(object):
    def __init__(self, url):
        self.url = url
        self.scrapper = Scrapper.get_scrapper_for_url(url)

    def process(self):
        self.scrapper.extract_metas()

    def get_datas(self):
        return self.scrapper.get_datas()
