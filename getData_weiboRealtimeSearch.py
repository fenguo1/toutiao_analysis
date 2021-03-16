from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from bs4 import BeautifulSoup
from time import gmtime, strftime


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
    for p in range(len(feeds)):
        topics_list.append(feeds[p].text);
        links_list.append(feeds[p].get_attribute('href'))
    for p in range(len(feeds)):

        f = open("./export_data/" + strftime("%d_%b_%Y_%H_%M", gmtime()) + "_" + str(p) + "_" +topics_list[p] + ".txt", 'a')
        f.write("url: "+ links_list[p])
        try:
            driver.get(links_list[p])
            userIDs = driver.find_elements_by_xpath('//div[@class="card-feed"]/div[@class="content"]/div[@class="info"]/div[2]/a[@class="name"]')#'/div[1]/a[@class="name"]')
                #print(len(userIDs))
            for h in range(len(userIDs)):
                f.write("userID:"+ userIDs[h].text + "; \t" + userIDs[h].get_attribute('href') + "\n")
        except Exception as e:
            print("[error]: path is not available: " + links_list[p])


        #driver.switch_to.window(driver.window_handles[0])
        #WebDriverWait(driver, 5)
        #driver.execute_script("window.history.go(-1)")
        f.close()
