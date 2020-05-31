import os,time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
#Opens target file and splits all the urls
#Go to https://www.youtube.com/subscription_manager and get the file
#Go to https://www.rssmix.com 
file = "/mnt/6708B5D108FCE57A/Downloads/subscription_manager"
readfile = open(file, "r",encoding="utf8")

def rssmix(results,number):
    options = Options()
    options.headless = False #Set to false if needed to actually see steps being performed
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
        print ("Loading took too much time!")


target = readfile.read()
i = 1
y = 1
results = []
while True:
    try:
        target = target.split('xmlUrl="',1)
        result = target[1].split('" />',1)[0]
        #print (result)
        results.append(result)
        target = target[1].split('" />',1)[1]
        i += 1
        if i>99:
            rss = rssmix(results,y)
            i = 1
            results = []
            print ("Part "+ str(y) + " ################################################################################################### " + "Part "+ str(y))
            print (rss)
            y += 1
    except:
        rss = rssmix(results,y)
        print ("Part "+ str(y) + " ################################################################################################### " + "Part "+ str(y))
        print (rss)
        print ("done,I guess")
        break