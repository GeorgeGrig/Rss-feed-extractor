#Go to https://takeout.google.com/takeout/custom/youtube 
#Click on 'All data included' then on 'Deselect all' then only 'Subscriptions' & click 'OK'
#Click 'Next step' & then on 'Create export'
#Click the 'Download' button after it appears
#Then extract the .json file from the downloaded zip file and get the file in the same folder as the script
#Run the script

import os,time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import json

with open("subscriptions.json", "r", encoding="utf8") as read_file:
    data = json.load(read_file)

def rssmix(results,number):
    options = Options()
    options.headless = True #Set to false if needed to actually see steps being performed
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.rssmix.com")
    for result in results:
        driver.find_element_by_xpath("/html/body/div[2]/form[1]/textarea").send_keys(result)
        driver.find_element_by_xpath("/html/body/div[2]/form[1]/textarea").send_keys(Keys.ENTER)
    driver.find_element_by_xpath("/html/body/div[2]/form[1]/input[2]").send_keys(f"Yt Part {number}")
    driver.find_element_by_xpath("/html/body/div[2]/form[1]/button").click()
    delay = 50 # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/h2[2]')))
        time.sleep(60)
        link = driver.find_element_by_xpath("/html/body/div[2]/p[1]/a").get_attribute('href')
        driver.close()
        return link
    except TimeoutException:
        driver.close()
        print ("Loading took too much time!")


i = 1
y = 1
results = []

#add all channel links to one list
for element in data:
    results.append("https://www.youtube.com/feeds/videos.xml?channel_id=" + element['snippet']['resourceId']['channelId'])

import collections
print(len([item for item, count in collections.Counter(results).items() if count > 1]))
#split this list in lists of 99 items
composite = [results[x:x+98] for x in range(0, len(results),98)]

for list in composite:
    rss = rssmix(list,y)
    print ("Part "+ str(y) + " ################################################################################################### " + "Part "+ str(y))
    print (rss)
    y += 1
print ("done,I guess")
