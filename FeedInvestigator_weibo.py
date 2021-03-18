from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from snownlp import SnowNLP
from time import gmtime, strftime
import csv
import re
import os

def findCSVs(strDir):
    csvFiles = []
    for file in os.listdir(strDir):
        if file.endswith(".csv"):
            csvFiles.append(os.path.join(strDir, file))
    return csvFiles

def readCSV(strFileName):
    listData = []
    with open(strFileName, newline='') as csvfile:
        csvDataRaw = csv.reader(csvfile, delimiter=' ', quotechar=',')
        #first row is topic
        #second row is url
        listData = list(csvDataRaw)
    return listData

csvFilesList = findCSVs('./export_data')
for f in range(len(csvFilesList)):
    data = (readCSV(csvFilesList[f]))
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
with webdriver.Chrome(options = opts) as driver:
    driver.minimize_window()
    for p in range(len(data)):
        f = open("./export_data/" + strftime("%d_%b_%Y_%H_%M", gmtime()) + "_" + str(p) + "_" +data[p][0] + ".txt", 'a')
        feeds_whiteboard = ""
        try:
            driver.get(data[p][1])
            userIDs = driver.find_elements_by_xpath('//div[@class="card-feed"]/div[@class="content"]/div[@class="info"]/div[2]/a[@class="name"]')#'/div[1]/a[@class="name"]')
            feeds_content = driver.find_elements_by_xpath('//div[@class="card-feed"]/div[@class="content"]/p[@class="txt"]')
#                #print(len(userIDs))
            FeedID_Weibo = "_"
            for h in range(len(userIDs)):
                f.write("userID:"+ userIDs[h].text + "; \t" + userIDs[h].get_attribute('href') + "\n")
                f.write("feed:" + feeds_content[h].text + "\n")
                feeds_whiteboard += feeds_content[h].text + "\n\n\n"
                # https://weibo.com/2110705772?refer_flag=1001030103_
                UserID_Weibo = re.findall(r'https://weibo.com/(.+)?\?refer_flag=',userIDs[h].get_attribute('href'))[0]
                tmp = re.findall(r'\?refer_flag=(.+)?_',userIDs[h].get_attribute('href'))[0]
                if("_" != FeedID_Weibo && tmp == FeedID_Weibo):
                    # not the first user comment, just add data to list
                if("_" != FeedID_Weibo && tmp != FeedID_Weibo):
                    # something goes wrong, there is different feedid been found!
                if("_" == FeedID_Weibo)
                    FeedID_Weibo = tmp
                #FeedTrackData = open("./export_data/" + strftime("%d_%b_%Y_%H_%M", gmtime()) + "_" + str(p) + "_" +data[p][0] + ".txt", 'a')
        except Exception as e:
            print("[error]: path is not available: " + str(e))
        f.close()
# opts = Options()
# #opts.add_argument("user-agent=[user-agent string]")
# # Below is tested line
# opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
# #This example requires Selenium WebDriver 3.13 or newer
# with webdriver.Chrome(options = opts) as driver:
#     driver.minimize_window()
#     WebDriverWait(driver, 0)
#     driver.get("https://s.weibo.com/top/summary?cate=realtimehot")
#     #driver.implicitly_wait(1000)
#     WebDriverWait(driver, 0)
#     feeds = driver.find_elements_by_xpath('//td[@class="td-02"]/a')
#     topics_list = []
#     links_list = []
#     with open('./export_data/data_' + strftime("%H_%M_%d_%b_%Y", gmtime()) + '.csv', 'w', newline='') as myfile:
#         wr = csv.writer(myfile, delimiter=' ', escapechar=' ',quoting=csv.QUOTE_NONE)
#         for p in range(len(feeds)):
#             topics_list.append(feeds[p].text);
#             #wr.writerow(topics_list[p])
#             links_list.append(feeds[p].get_attribute('href'))
#             wr.writerow([topics_list[p], links_list[p]])
#     if 0:
#     #for p in range(len(feeds)):
#
#         f = open("./export_data/" + strftime("%d_%b_%Y_%H_%M", gmtime()) + "_" + str(p) + "_" +topics_list[p] + ".txt", 'a')
#         f.write("url: "+ links_list[p])
#         feeds_whiteboard = ""
#         try:
#             driver.get(links_list[p])
#             userIDs = driver.find_elements_by_xpath('//div[@class="card-feed"]/div[@class="content"]/div[@class="info"]/div[2]/a[@class="name"]')#'/div[1]/a[@class="name"]')
#             feeds_content = driver.find_elements_by_xpath('//div[@class="card-feed"]/div[@class="content"]/p[@class="txt"]')
#                 #print(len(userIDs))
#
#             for h in range(len(userIDs)):
#                 f.write("userID:"+ userIDs[h].text + "; \t" + userIDs[h].get_attribute('href') + "\n")
#                 f.write("feed:" + feeds_content[h].text + "\n")
#                 feeds_whiteboard += feeds_content[h].text + "\n\n\n"
#
#
#         except Exception as e:
#             print("[error]: path is not available: " + links_list[p])
#         if feeds_whiteboard:
#             s = SnowNLP(feeds_whiteboard)
#             print(*s.keywords(5))
#
#         #driver.switch_to.window(driver.window_handles[0])
#         #WebDriverWait(driver, 5)
#         #driver.execute_script("window.history.go(-1)")
#         f.close()
