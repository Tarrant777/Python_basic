from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time

# driver = webdriver.PhantomJS("./driver/phantomjs/bin/phantomjs")
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
# driver.get("http://www.javascriptobfuscator.com/Javascript-Obfuscator.aspx")
driver.get("https://trends.google.com.tw/trends/hottrends#pn=p12")

for i in range(0, 1):
    time.sleep(3)
    day_search = driver.find_elements_by_class_name("hottrends-trends-list-date-container")
    print(day_search)
    for single_day_search in day_search:
        single_date = (single_day_search.find_element_by_class_name("hottrends-trends-list-date-header-text").text)
        if single_date != "":
            print("----", single_date, "----")
            item = single_day_search.find_elements_by_class_name("hottrends-trends-list-trend-container")
            for single_search_item in item:
                title = single_search_item.find_element_by_class_name("hottrends-single-trend-title").text
                search_times = single_search_item.find_element_by_class_name(
                    "hottrends-single-trend-info-line-number").text
                print(title, search_times)
    button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "more-link")))
    button.click()

driver.close()
