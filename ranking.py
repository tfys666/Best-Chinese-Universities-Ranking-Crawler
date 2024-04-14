import requests
from bs4 import BeautifulSoup

class RankingScraper:
    def __init__(self, url):
        self.url = url
        self.table_data = []

    def get_html(self):
        try:
            r = requests.get(self.url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            self.htmdata = r.text
        except Exception as e:
            print(f'爬虫异常! {e}')
            self.htmdata = None

    def parse_html(self):
        if self.htmdata:
            soup = BeautifulSoup(self.htmdata, 'html.parser')
            for tr in soup.find('tbody').children:
                if tr.name == 'tr':
                    tdslist = tr.find_all('td')
                    tds1 = tdslist[0].string.strip()
                    tds2 = tdslist[1].find('a').string.strip() if tdslist[1].find('a') else ''
                    tds3 = tdslist[2].get_text(strip=True)
                    tds4 = tdslist[3].get_text(strip=True)
                    tds5 = tdslist[4].get_text(strip=True)
                    self.table_data.append([tds1, tds2, tds3, tds4, tds5])

    def print_table(self):
        for row in self.table_data:
            print(row)

