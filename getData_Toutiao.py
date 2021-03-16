from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
opts = Options()
#opts.add_argument("user-agent=[user-agent string]")
# Below is tested line
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome(options = opts) as driver:
    WebDriverWait(driver, 0)
    driver.get("https://news.sina.com.cn/")
    driver.implicitly_wait(1000)
    WebDriverWait(driver, 0)
    feeds = driver.find_elements_by_xpath('//a[@class="linkNewsTopBold"]')
    #feeds_list = []
    for p in range(len(feeds)):
        print(feeds[p].text)
