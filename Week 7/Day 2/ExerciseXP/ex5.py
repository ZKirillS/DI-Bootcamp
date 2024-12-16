# Exercise 5 : Scrape and Analyze Weather Data from a JavaScript-Enabled Weather Website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
    url = "https://www.accuweather.com"
    driver.get(url)

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search-input"))
    )
    search_box.send_keys("Bat Yam")
    
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    bat_yam_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'Bat+Yam')]"))
    )
    bat_yam_link.click()
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # element = driver.find_element(By.CLASS_NAME, class_="daily-list content-module")
    days = soup.find_all("a", class_="daily-list-item")  
    weather_data = []

    for day in days:
        day_label = day.find("p", class_="day").text.strip()  
        temperature = day.find("span", class_="temp-hi").text.strip()
        temperature = int(temperature.replace("°", "")) 
        condition = day.find("p", class_="no-wrap").text.strip()
        weather_data.append({"Day": day_label, "Temperature": temperature, "Condition": condition})

finally:
    driver.quit()

df = pd.DataFrame(weather_data)
average_temperature = df["Temperature"].mean()
most_common_condition = df["Condition"].mode()[0]
print("Weather Data:")
print(df)
print("\nAnalysis:")
print(f"Average Temperature: {average_temperature:.2f}°C")
print(f"Most Common Condition: {most_common_condition}")