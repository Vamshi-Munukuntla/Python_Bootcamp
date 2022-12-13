
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\vamsh\Downloads\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
new_driver = webdriver.Chrome(service=service)
url = "https://www.amazon.com/Data-Structures-Algorithms-Swift-Dictionaries-ebook/dp/B086GWMSXB/ref=sr_1_1?qid" \
      "=1670923801&refinements=p_27%3AElshad+Karimov&s=books&sr=1-1 "
new_driver.get(url)

# price = new_driver.find_element(by=By.ID,
#                                 value="kindle-rental-price-column")
# print(price.text)

# careers = new_driver.find_element(by=By.XPATH,
                                  # value='//*[@id="navFooter"]/div[1]/div/div[1]/ul/li[1]/a')
# print(careers.get_attribute('href'))


new_driver.quit()