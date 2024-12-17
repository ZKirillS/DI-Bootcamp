# Scraping Data from a Dynamic Webpage
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
    url = "https://www.inmotionhosting.com"
    driver.get(url)
    
    element = driver.find_element(By.XPATH, "//a[@href='/shared-hosting']")
    driver.execute_script("arguments[0].click();", element)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "imh-rostrum-card"))
    )
    time.sleep(3)
    soup1 = BeautifulSoup(driver.page_source, "html.parser")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '1 Month')]"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "imh-rostrum-card"))
    )
    time.sleep(3)
    soup2 = BeautifulSoup(driver.page_source, "html.parser")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '3 Year')]"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "imh-rostrum-card"))
    )
    time.sleep(3)
    soup3 = BeautifulSoup(driver.page_source, "html.parser")
    time.sleep(3)
    plans_year = soup1.find_all("div", class_="imh-rostrum-card")  
    plans_data_year = []

    for plan in plans_year:
        plan_name = plan.find("h3").get_text(strip=True) if plan.find("h3") else "N/A"
        save_percentage = plan.find("span", class_="dnt").get_text(strip=True) if plan.find("span", class_="dnt") else "N/A"
        prices = plan.find("div", class_="imh-pricing-container connected-switcher")
        price_save = prices.find("div", class_="imh-rostrum-starting-at-price-discounted")
        price_normal = prices.find("div", class_="imh-rostrum-starting-at-price-normal")
        price = price_save.find("span", class_="rostrum-price").get_text(strip=True) if price_save.find("span", class_="rostrum-price") else "N/A"
        renew_price = price_normal.find("span", class_="rostrum-price").get_text(strip=True) if price_normal.find("span", class_="rostrum-price") else "N/A"
        description = plan.find("div", class_="imh-rostrum-sub-title").get_text(strip=True) if plan.find("div", class_="imh-rostrum-sub-title") else "N/A"
        period = "1 Year"
        plans_data_year.append({
            "Name": plan_name,
            f"Price_{period}_Disc": price,
            f"Price_{period}_Normal": renew_price,
            f"Save_{period}": save_percentage,
            "Description": description,
            "Period":period
        })
    

    plans_month = soup2.find_all("div", class_="imh-rostrum-card")  
    plans_data_month = []

    for plan in plans_month:
        plan_name = plan.find("h3").get_text(strip=True) if plan.find("h3") else "N/A"
        save_percentage = plan.find("span", class_="dnt").get_text(strip=True) if plan.find("span", class_="dnt") else "N/A"
        prices = plan.find("div", class_="imh-pricing-container connected-switcher")
        price_save = prices.find("div", class_="imh-rostrum-starting-at-price-discounted")
        price_normal = prices.find("div", class_="imh-rostrum-starting-at-price-normal")
        price = price_save.find("span", class_="rostrum-price").get_text(strip=True) if price_save.find("span", class_="rostrum-price") else "N/A"
        renew_price = price_normal.find("span", class_="rostrum-price").get_text(strip=True) if price_normal.find("span", class_="rostrum-price") else "N/A"
        description = plan.find("div", class_="imh-rostrum-sub-title").get_text(strip=True) if plan.find("div", class_="imh-rostrum-sub-title") else "N/A"
        period = "1 Month"
        plans_data_month.append({
            "Name": plan_name,
            f"Price_{period}_Disc": price,
            f"Price_{period}_Normal": renew_price,
            f"Save_{period}": save_percentage,
            "Description": description,
            "Period":period
        })
    
    plans_3_year = soup3.find_all("div", class_="imh-rostrum-card")  
    plans_data_3_year = []

    for plan in plans_3_year:
        plan_name = plan.find("h3").get_text(strip=True) if plan.find("h3") else "N/A"
        save_percentage = plan.find("span", class_="dnt").get_text(strip=True) if plan.find("span", class_="dnt") else "N/A"
        prices = plan.find("div", class_="imh-pricing-container connected-switcher")
        price_save = prices.find("div", class_="imh-rostrum-starting-at-price-discounted")
        price_normal = prices.find("div", class_="imh-rostrum-starting-at-price-normal")
        price = price_save.find("span", class_="rostrum-price").get_text(strip=True) if price_save.find("span", class_="rostrum-price") else "N/A"
        renew_price = price_normal.find("span", class_="rostrum-price").get_text(strip=True) if price_normal.find("span", class_="rostrum-price") else "N/A"
        description = plan.find("div", class_="imh-rostrum-sub-title").get_text(strip=True) if plan.find("div", class_="imh-rostrum-sub-title") else "N/A"
        period = "3 Year"
        plans_data_3_year.append({
            "Name": plan_name,
            f"Price_{period}_Disc": price,
            f"Price_{period}_Normal": renew_price,
            f"Save_{period}": save_percentage,
            "Description": description,
            "Period":period
        })

        df_month = pd.DataFrame(plans_data_month)
        df_year = pd.DataFrame(plans_data_year)
        df_3_years = pd.DataFrame(plans_data_3_year)
        merged_df = df_month.merge(df_year, on="Name").merge(df_3_years, on="Name")
        print(merged_df)
        merged_df.to_csv("hosting_plans.csv", index=False)
        print("Data saved to hosting_plans.csv")

finally:
    driver.quit()
