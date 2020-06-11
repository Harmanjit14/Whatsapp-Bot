from selenium import webdriver
import time
import re


victom = input("Enter contact of the victom : ")
msg = input("Enter MSG to be sent : ")
limit = int(input("Enter no of times you want to attact the victom : "))

driver = webdriver.Chrome("./chromedriver")
driver.get("http://web.whatsapp.com/")
time.sleep(5)


driver.find_element_by_class_name("_3FeAD"+r'(\.\s)'+"uu8jX").send_keys(victom)
driver.find_element_by_css_selector("span[title="+victom+"]").click()
for _ in range(limit):
    driver.find_element_by_class_name("_13mgZ").send_keys(msg)
    driver.find_element_by_class_name("_3M-N-").click()