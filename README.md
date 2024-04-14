# Best-Chinese-Universities-Ranking-Crawler
This Python script uses the `requests` and `BeautifulSoup` libraries to scrape ranking data from a specified URL and prints it in a table format.
## Usage
1. Import the `RankingScraper` class from the `ranking` module.
2. Create an instance of the `RankingScraper` class with the desired URL as the argument.
3. Call the `get_html` method to fetch the HTML content of the URL.
4. Call the `parse_html` method to parse the HTML content and extract the ranking data.
5. Call the `print_table` method to print the extracted ranking data in a table format.
## Example
```python
from ranking import RankingScraper
url = 'https://www.shanghairanking.cn/rankings/bcur/202311'
scraper = RankingScraper(url)
scraper.get_html()
scraper.parse_html()
scraper.print_table()
```
Replace the `url` variable with the desired URL containing the ranking data you want to scrape.
