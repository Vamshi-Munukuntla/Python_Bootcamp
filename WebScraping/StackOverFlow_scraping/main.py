import requests
from bs4 import BeautifulSoup

website = "https://stackoverflow.com"
url = "https://stackoverflow.com/?tab=hot"
response = requests.get(url)
# print(response)
stackoverflow = response.text

new_soup = BeautifulSoup(stackoverflow, 'html.parser')
question_tag = new_soup.find(name='h3', class_="s-post-summary--content-title")
question_title = question_tag.getText().strip()
question_link = website+question_tag.find(name='a').get('href')
question_vote = new_soup.find(name="div", class_="s-post-summary--stats-item s-post-summary--stats-item__emphasized")
#
# print(question_title)
# print(question_link)
# print(question_vote)
vote = question_vote.find(name='span', class_="s-post-summary--stats-item-number").getText()
print(vote)