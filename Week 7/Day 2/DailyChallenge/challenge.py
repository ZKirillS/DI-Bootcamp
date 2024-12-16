from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-features=MediaCapabilities")
options.add_argument("--lang=en")
driver = webdriver.Chrome(options=options)


try:
    url = "https://www.bbc.com/weather/293397"
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "wr-day"))
    )
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    days = soup.find_all("li", class_="wr-day")

    weather_data = []

    for day in days:
        day_name = day.find("span", class_="wr-date__longish")
        day_name = day_name.text.strip() if day_name else "Tonight"
        day_temp = day.find('div', class_="wr-day__temperature")
        temp_high_div = day_temp.find("div", class_="wr-day-temperature__high") if day_temp else "N/A"

        temp_high = temp_high_div.find("span", class_="wr-value--temperature--c").text.strip() if temp_high_div else "N/A"
        temp_low_div = day.find("div", class_="wr-day-temperature__low")

        temp_low = temp_low_div.find("span", class_="wr-value--temperature--c").text.strip() if temp_high_div else "N/A"

        condition = day.find("div", class_="wr-weather-type__text").text.strip() 

        weather_data.append({
            "Day": day_name,
            "High Temperature (°C)": temp_high,
            "Low Temperature (°C)": temp_low,
            "Condition": condition
        })

    df = pd.DataFrame(weather_data)

    df.to_csv("bbc_weather_bat_yam.csv", index=False)

    print(df)

finally:
    driver.quit()