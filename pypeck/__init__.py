from .scrapper import Scrapper


class PyPeck(object):
    def __init__(self, url):
        self.url = url
        self.scrapper = Scrapper.get_scrapper_for_url(url)

    def process(self):
        pass





