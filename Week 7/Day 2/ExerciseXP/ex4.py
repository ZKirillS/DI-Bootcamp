from selenium import webdriver
from bs4 import BeautifulSoup
import time
from collections import defaultdict
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_argument("--headless") 
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-features=MediaCapabilities") 
options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=options)

url = "https://www.bbc.com/innovation/technology"
driver.get(url)

time.sleep(5)

html_content = driver.page_source

soup = BeautifulSoup(html_content, 'html.parser')
print('Success')
driver.quit()

articles = []

article_blocks = soup.find_all("div", {"data-testid": "liverpool-card"})
print(f"Number of article blocks found: {len(article_blocks)}")  # Debugging line

for article in article_blocks:

    title = article.find("h2", {"data-testid": "card-headline"}).get_text(strip=True)
    
    date_str = article.find("span",  {"data-testid": "card-metadata-lastupdated"}).get_text(strip=True)
    
    dict1 = {'title': title, 'date':date_str}
    articles.append(dict1)
print('Success')
print(articles)