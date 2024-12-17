from selenium import webdriver
from selenium.webdriver.common.by import By
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
    url = "https://www.scrapethissite.com/pages/frames/"
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "iframe"))
    )
    driver.switch_to.frame("iframe")

    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "row")))
    rows = driver.find_elements(By.CLASS_NAME, "row")
    turtle_data = []

    for row_index, row in enumerate(rows):
        family_cards = row.find_elements(By.CLASS_NAME, "col-md-4")
        for card_index in range(len(family_cards)):
            learn_more_button = WebDriverWait(family_cards[card_index], 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "btn-default"))
            )
            learn_more_button.click()

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "family-name"))
            )
            soup = BeautifulSoup(driver.page_source, "html.parser")
            time.sleep(2)

            name = soup.find("h3", class_="family-name").get_text(strip=True)
            description = soup.find("p", class_="lead")
            if description:
                family_name = description.find("span", class_="family-name").get_text(strip=True) if description.find("span", class_="family-name") else ""
                common_name = description.find("strong", class_="common-name").get_text(strip=True) if description.find("strong", class_="common-name") else ""
                description = f"The {family_name} family of turtles — more commonly known as \"{common_name}\" — was first discovered in 1887 by Boulenger."
            else:
                description = "Description not found"

            turtle_data.append({"name": name, "description": description})
                    
            back_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "btn-xs"))
            )
            back_button.click()

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "turtle-family-card"))
            )

            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "col-md-4")))
            family_cards = driver.find_elements(By.CLASS_NAME, "col-md-4")
            print(f"Found {len(family_cards)} cards.")
         
            time.sleep(2)  
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "row")))
        rows = driver.find_elements(By.CLASS_NAME, "row")  
        time.sleep(2)
        
    df = pd.DataFrame(turtle_data)
    df.to_csv("turtle_data.csv", index=False)

finally:
    driver.quit()
