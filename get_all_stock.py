import requests
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup

from configure import STOCKS_LIST


class Parse():
    def __init__(self):
        self.stocks_list = STOCKS_LIST
        self.request = requests.session()
        self.request.mount('http://', HTTPAdapter(max_retries=3))
        self.request.mount('https://', HTTPAdapter(max_retries=3))

    def yield_urls(slef, url, num_Of_pages=1):
        for i in range(1, num_Of_pages+1):
            urls = url % i
            yield urls

    def request_get_urls(self):
        urls = self.yield_urls(self.stocks_list)
        for url in urls:
            html_content = self.request_get_url(url)
            self.parse_html_content(html_content)

    def request_get_url(self, url):
        r = self.request.get(url, timeout=5)
        return r.text

    def parse_html_content(self, html):
        soup = BeautifulSoup(html, 'lxml')
        titles = soup.select('table > thead > tr')
        for title in titles:
            item_soup = BeautifulSoup(str(title), 'lxml')
            ths = item_soup.select('th')
            print(ths[0].text,
                  ths[1].text,
                  '网址',
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


# 序号 代码 网址 名称 现价 涨跌幅(%) 换手(%) 成交额 流通市值
# 1 301408 http://stockpage.10jqka.com.cn/301408/ N华人 25.31 55.85 64.48 9.48亿 14.26亿
# 2 688522 http://stockpage.10jqka.com.cn/688522/ N纳睿 60.40 29.39 70.71 14.56亿 21.62亿
# 3 688004 http://stockpage.10jqka.com.cn/688004/ 博汇科技 33.95 20.01 17.88 2.30亿 13.53亿
# 4 300079 http://stockpage.10jqka.com.cn/300079/ 数码视讯 7.08 20.00 19.92 16.75亿 89.70亿
# 5 688039 http://stockpage.10jqka.com.cn/688039/ 当虹科技 65.94 20.00 11.85 4.25亿 38.75亿
# 6 300588 http://stockpage.10jqka.com.cn/300588/ 熙菱信息 12.68 19.96 10.89 1.83亿 17.29亿
# 7 688292 http://stockpage.10jqka.com.cn/688292/ 浩瀚深度 31.97 19.74 21.08 2.29亿 11.55亿
# 8 688418 http://stockpage.10jqka.com.cn/688418/ 震有科技 15.46 13.68 11.40 2.22亿 20.50亿
# 9 300418 http://stockpage.10jqka.com.cn/300418/ 昆仑万维 25.21 13.56 16.22 42.52亿 272.16亿
# 10 300597 http://stockpage.10jqka.com.cn/300597/ 吉大通信 9.97 12.91 16.08 3.48亿 22.21亿
# 11 300380 http://stockpage.10jqka.com.cn/300380/ 安硕信息 18.77 12.46 11.44 2.66亿 23.52亿
# 12 688579 http://stockpage.10jqka.com.cn/688579/ 山大地纬 12.02 11.92 8.62 2.83亿 33.86亿
# 13 300212 http://stockpage.10jqka.com.cn/300212/ 易华录 27.52 11.60 12.67 21.66亿 176.33亿
# 14 688095 http://stockpage.10jqka.com.cn/688095/ 福昕软件 90.60 11.58 5.90 2.07亿 36.13亿
# 15 688521 http://stockpage.10jqka.com.cn/688521/ 芯原股份-U 69.57 10.50 7.12 9.96亿 145.19亿
# 16 688607 http://stockpage.10jqka.com.cn/688607/ 康众医疗 26.01 10.35 7.75 1.32亿 17.30亿
# 17 300058 http://stockpage.10jqka.com.cn/300058/ 蓝色光标 6.20 10.32 10.03 13.95亿 143.78亿
# 18 002219 http://stockpage.10jqka.com.cn/002219/ 新里程 5.03 10.07 4.71 7.54亿 163.13亿
# 19 601566 http://stockpage.10jqka.com.cn/601566/ 九牧王 12.60 10.04 8.14 5.72亿 72.40亿
# 20 603803 http://stockpage.10jqka.com.cn/603803/ 瑞斯康达 8.44 10.04 3.98 1.39亿 35.54亿
