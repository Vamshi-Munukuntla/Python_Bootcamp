# TODO 1 - Open amazon search link and parse it
# TODO 2 - Create new excel file with two columns - title and rating
# TODO 3 - Parse html file to get title and rating of the product
# TODO 4 - Save all rows to excel file
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

ACCEPT_LANGUAGE = "en-US,en;q=0.9"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/95.0.4638.69 Safari/537.36 "

HEADERS = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT
}

URL = "https://www.amazon.com/s?k=airpods"
response = requests.get(URL, headers=HEADERS)
amazon = response.text
# print(amazon)

new_soup = BeautifulSoup(amazon, 'html.parser')
product_list = new_soup.find_all(name='div', class_='sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right')
workbook = Workbook()
sheet = workbook.active
sheet['A1'] = 'Title'
sheet['B1'] = 'Rating'
row = 2
for product in product_list:
    product_name = product.find(name='span', class_="a-size-medium a-color-base a-text-normal").getText()
    rating = product.find(name='div', class_='a-row a-size-small').getText()
    sheet["A"+str(row)] = product_name
    sheet['B'+str(row)] = rating
    row += 1

workbook.save('amazon_output.xlsx')
