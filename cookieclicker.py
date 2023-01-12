from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import keyboard

# setting up Selenium and Web Driver
s = Service("C:/Users/Kelly/Documents/code/Python Bootcamp/chromedriver.exe")
# keeps the window open
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options=chrome_option)
# opens cookie clicker in Chrome webpage
driver.get("https://orteil.dashnet.org/cookieclicker/")


def check_products():
    """checks the store for product upgrades and buys it as soon as it is available"""
    # checks if there are any products available (i.e. there are enough cookies to purchase an upgrade)
    try:
        avail_products = (driver.find_elements(By.CLASS_NAME, "enabled"))
        # loops through list of available products backwards and buys the most expensive first
        for x in avail_products[::-1]:
            x.click()
    # nothing happens if no products are available
    except:
        pass


def click_cookie():
    """clicks on the cookie"""
    try:
        driver.find_element(By.ID, "bigCookie").click()
    # if cookie cannot be clicked because another function is being called on, do nothing
    except:
        pass


# wait for the Select Language prompt to finish loading
if WebDriverWait(driver, timeout=3).until(ec.element_to_be_clickable((By.ID, "langSelect-EN"))):
    # selects language
    driver.find_element(By.ID, "langSelect-EN").click()
    # repeatedly check for products and clicks on the cookie
    while True:
        check_products()
        click_cookie()
        # exits webpage and closes  webdriver when ESC is pressed
        if keyboard.is_pressed('Esc'):
            driver.quit()
