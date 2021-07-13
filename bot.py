from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver") 
driver.get("https://twitter.com/login")
sleep(3)
driver.find_element_by_name("session[username_or_email]").send_keys("suniltweetbot1")
driver.find_element_by_name("session[password]").send_keys("asnasosu14325")
driver.find_element_by_name("session[password]").send_keys(Keys.RETURN)
sleep(3)

file = open('test_tweet.txt', 'r')
for word in file:
    if word == "\n":
        continue
    driver.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
    sleep(1)
    driver.find_element_by_class_name("notranslate").click()
    driver.find_element_by_class_name("notranslate").send_keys(word)
    driver.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
    sleep(1)

file.close()