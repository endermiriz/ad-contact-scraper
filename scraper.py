import time
import undetected_chromedriver as uc

from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import requests

def run():
    options = uc.ChromeOptions()

    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--auto-open-devtools-for-tabs")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(r"--user-data-dir=\Users\Ender\AppData\Local\Google\Chrome")
    options.add_argument("--profile-directory=Profile 4")
    # options.add_argument('--headless')
    # options.add_argument("--headless=new")
    driver = uc.Chrome(options=options)

    driver.get('https://www.sahibinden.com/fiat-egea?pagingSize=50')
    tablerows = driver.find_element(By.XPATH,"//table[@id='searchResultsTable']/tbody")
    node = driver.find_element(By.CSS_SELECTOR, "#searchResultsTable > tbody > tr:nth-child(1)")
    for row in range(1,50):
        try:
            link = driver.find_element(By.CSS_SELECTOR,"#searchResultsTable > tbody > tr:nth-child({}) > td.searchResultsTitleValue > a.classifiedTitle".format(row)).get_attribute('href')
            print(link)
            new_tab(driver,link)
        except NoSuchElementException:
            pass

def new_tab(driver,link):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)
    get_number(driver)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return

def get_number(driver):
    number = driver.find_element(By.CSS_SELECTOR,"#phoneInfoPart > li > span.pretty-phone-part.show-part")
    if number.text == "":
        number = driver.find_element(By.CSS_SELECTOR,"#phoneInfoPart > li > span.pretty-phone-part.show-part > span").get_attribute('data-content')
        print(number)
    else:
        number = number.text
        print(number)
    replace_number(number)


    return

def replace_number(number):
    n1 = number.replace('(', '')
    n2 = n1.replace(')', '')
    n3 = n2.replace(' ', '')
    sendmessage_request(n3)
    return

def sendmessage_request(number):
    url = "http://localhost:3000/sendmessage"
    json_message = {"number":"9{}".format(number),"message":"Merhaba araç ilanınız için yazıyorum, hala satılık mı?"}
    requests.post(url, json=json_message)
    return

if __name__ == "__main__":
    run()