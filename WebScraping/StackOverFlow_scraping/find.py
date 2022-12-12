import requests
from bs4 import BeautifulSoup

website = "https://stackoverflow.com"
url = "https://stackoverflow.com/?tab=hot"
response = requests.get(url)
# print(response)
stackoverflow = response.text

new_soup = BeautifulSoup(stackoverflow, 'html.parser')
question_tag = new_soup.find_all(name='h3', class_="s-post-summary--content-title")
question_titles = []
question_links = []
for i in question_tag:
    title = i.getText().strip()
    question_titles.append(title)
    link = website + i.find(name='a').get('href')
    question_links.append(link)

question_vote = new_soup.find_all(name="div", class_="s-post-summary--stats-item s-post-summary--stats-item__emphasized")
votes = []
for i in question_vote:
    votes.append(i.find(name='span', class_="s-post-summary--stats-item-number").getText())

largest_vote = max(votes)
index = votes.index(largest_vote)
print(question_titles[index])
print(question_links[index])
print(votes[index])