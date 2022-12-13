from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pprint


chrome_driver_path = r"C:\Users\vamsh\Downloads\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
new_driver = webdriver.Chrome(service=service)
new_driver.get('https://hoopshype.com/salaries/players/')

# players = new_driver.find_elements(by=By.CLASS_NAME,
#                                  value='name')
# salaries = new_driver.find_elements(by=By.CLASS_NAME,
#                                  value="hh-salaries-sorted")
# salaries_dict = {}
# for i in range(1, len(players)):
#     salaries_dict[i] = {
#         "name": players[i].text,
#         "amount":salaries[i].text
#     }
# pprint.pprint(salaries_dict)


# facebook_share = new_driver.find_element(by=By.ID, value='share-facebook')
# facebook_share.click()

# player_details = new_driver.find_element(by=By.LINK_TEXT,
#                                          value='Stephen Curry')
# player_details.click()

search = new_driver.find_element(by=By.CLASS_NAME, value="branding__search-form")
search.click()
search_bar = new_driver.find_element(by=By.NAME, value="s")
search_bar.send_keys('John Wall')
search_bar.send_keys(Keys.ENTER)
# new_driver.close()
