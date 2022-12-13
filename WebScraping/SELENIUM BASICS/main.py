from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\Users\vamsh\Downloads\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
new_driver = webdriver.Chrome(service=service)
new_driver.get('https://stackoverflow.com/?tab=hot')
# title = new_driver.find_element(by=By.CLASS_NAME,
#                                 value="s-post-summary--content-title")
# print(title.text)\
# search_bar = new_driver.find_element(by=By.NAME, value='q')
# print(search_bar.get_attribute('placeholder'))
search = new_driver.find_element(by=By.NAME, value='q')
# print(search.get_attribute('placeholder'))
# print(search.location)  # To look for any location of the element in the script.
# search.send_keys('regex')
# time.sleep(1)
# search.clear()
# print(search.is_enabled())

# TODO - Scrolling the page down till the end
# html = new_driver.find_element(by=By.TAG_NAME,
#                                value='html')
# html.send_keys(Keys.END)
# time.sleep(2)
# html.send_keys(Keys.HOME)
# time.sleep(2)


week = new_driver.find_element(by=By.LINK_TEXT, value='Week')
week.click()
time.sleep(3)
new_driver.back()
time.sleep(2)
new_driver.forward()
time.sleep(1)
