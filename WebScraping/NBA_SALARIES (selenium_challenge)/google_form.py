from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\Users\vamsh\Downloads\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
new_driver = webdriver.Chrome(service=service)
new_driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeQvVOm_I11CAcX6_eMrnFWjjG-UKs0F30eQqbuczfufeLQeg/viewform')
time.sleep(1)
my_details = ["Vamshi", "Munukuntla", "vamshi.kumar59@gmail.com"]
text_boxes = new_driver.find_elements(by=By.CLASS_NAME, value="whsOnd.zHQkBf")
for i in range(len(text_boxes)):
    text_boxes[i].send_keys(my_details[i])
    time.sleep(1)

submit = new_driver.find_element(by=By.CLASS_NAME, value="NPEfkd.RveJvd.snByac")
submit.click()
time.sleep(1)
# whsOnd zHQkBf
