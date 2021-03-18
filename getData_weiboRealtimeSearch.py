from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from time import gmtime, strftime
import csv


opts = Options()
#opts.add_argument("user-agent=[user-agent string]")
# Below is tested line
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome(options = opts) as driver:
    driver.minimize_window()
    WebDriverWait(driver, 0)
    driver.get("https://s.weibo.com/top/summary?cate=realtimehot")
    #driver.implicitly_wait(1000)
    WebDriverWait(driver, 0)
    feeds = driver.find_elements_by_xpath('//td[@class="td-02"]/a')
    topics_list = []
    links_list = []
    with open('./export_data/data_' + strftime("%H_%M_%d_%b_%Y", gmtime()) + '.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, delimiter=' ', escapechar=' ',quoting=csv.QUOTE_NONE)
        for p in range(len(feeds)):
            topics_list.append(feeds[p].text);
            #wr.writerow(topics_list[p])
            links_list.append(feeds[p].get_attribute('href'))
            wr.writerow([topics_list[p], links_list[p]])
