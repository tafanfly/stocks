import time
import random
import requests
from requests.adapters import HTTPAdapter

HEADERS = [
    {}
]

class requestUrl(object):
    def __init__(self):
        self.request = requests.session()
        self.request.mount('http://', HTTPAdapter(max_retries=3))
        self.request.mount('https://', HTTPAdapter(max_retries=3))

    def request_get(self):
        time.sleep(random.random())
        r = self.request.get(url, headers = headers, proxies=proxies, timeout=4)

