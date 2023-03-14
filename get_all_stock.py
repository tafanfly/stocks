import requests
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup

from configure import STOCKS_LIST
from create_html import renderHtmlTable


class Parse():
    def __init__(self):
        self.table = renderHtmlTable()
        self.stocks_list = STOCKS_LIST
        self.request = requests.session()
        self.request.mount('http://', HTTPAdapter(max_retries=3))
        self.request.mount('https://', HTTPAdapter(max_retries=3))

    def yield_urls(slef, url, num_of_pages=5):
        for i in range(1, num_of_pages+1):
            urls = url % i
            yield urls

    def request_get_urls(self):
        urls = self.yield_urls(self.stocks_list)
        for url in urls:
            print(url)
            html_content = self.request_get_url(url)
            print(html_content)
            self.parse_html_content(html_content)

    def request_get_url(self, url):
        r = self.request.get(url, timeout=5)
        if r.status_code != 200 or (not r.text):
            print(f"WRN: status code is {r.status_code} and text is {r.text}")
        return r.text

    def parse_html_content(self, html):
        soup = BeautifulSoup(html, 'lxml')
        titles = soup.select('table > thead > tr')
        for title in titles:
            item_soup = BeautifulSoup(str(title), 'lxml')
            ths = item_soup.select('th')
            print (ths[0].text,
                      ths[1].text,
                      "网址",
                      ths[2].text,
                      ths[3].text,
                      ths[4].text,
                      ths[7].text,
                      ths[10].text,
                      ths[12].text)


        items = soup.select('table > tbody > tr')
        for item in items:
            item_soup = BeautifulSoup(str(item), 'lxml')
            ths = item_soup.select('td')
            print(ths[0].text,
                  ths[1].text,
                  ths[1].select('a')[0].attrs['href'],
                  ths[2].text,
                  ths[3].text,
                  ths[4].text,
                  ths[7].text,
                  ths[10].text,
                  ths[12].text)


parse = Parse()
parse.request_get_urls()
