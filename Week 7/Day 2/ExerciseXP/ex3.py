from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

url = "https://www.rottentomatoes.com/browse/movies_at_home/critics:certified_fresh"
driver.get(url)
time.sleep(3)
html_content = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

movies = []
movie_blocks = html_content.find_all("div", class_="flex-container")

for movie in movie_blocks:
    title = movie.find("span", class_="p--small").get_text(strip=True) 
    release_date = movie.find("span", class_="smaller").get_text(strip=True)

    movies.append({
        "Title": title,
        "Release Date": release_date
    })

df = pd.DataFrame(movies)
print(df)