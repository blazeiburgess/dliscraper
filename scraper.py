from requests import get
from lxml.html import fromstring
from json import dump
class Scraper(object):
    course_url_template = "https://www.livelingua.com/{language}/courses/"
    base_url = "https://www.livelingua.com"
    def __init__(self, language):
        self.language = language
        self.course_url = self.course_url_template.format(
                language=language
            )

    def _get_course_pages(self):
        page = get(self.course_url)
        etree = fromstring(page.content)
        return etree.xpath("//h6//a[@title]/@href")

    def __get_ebooks(self, etree):
        return etree.xpath("//div/select[@onchange]/option/@value") + \
                etree.xpath("//iframe[@id='ebookReader']/@src")

    def __get_audio(self, etree):
        return [
            {
                "url": self.base_url + audio.xpath("source/@src")[0], 
                "name": audio.xpath("@title")[0]
            } for audio in etree.xpath("//div/audio")
        ]


    def _get_course_page_data(self, url):
        data = {}
        page = get(url)
        etree = fromstring(page.content)
        data['course_name'] = etree.xpath("//title/text()")[0].split("::")[0].strip()
        data['ebooks'] = self.__get_ebooks(etree)
        data['audio'] = self.__get_audio(etree)        
        if not data['ebooks'] and not data['audio']:
            import pdb; pdb.set_trace()
            raise ValueError(f"No ebooks or audio found for url {url}")
        return data

    def dump_data(self, course_data):
        with open(f"course_data/{self.language}.json","w") as f:
            dump(course_data, f, indent=2)

    def scrape(self):
        course_data = []
        for course_url in self._get_course_pages():
            course_data.append(self._get_course_page_data(course_url))
            self.dump_data(course_data)

