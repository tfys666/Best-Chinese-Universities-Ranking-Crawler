from ranking import RankingScraper

url = 'https://www.shanghairanking.cn/rankings/bcur/202311'
scraper = RankingScraper(url)

scraper.get_html()
scraper.parse_html()
scraper.print_table()