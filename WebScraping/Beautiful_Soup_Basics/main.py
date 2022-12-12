from bs4 import BeautifulSoup

with open('home.html') as file:
    content = file.read()

new_soup = BeautifulSoup(content, 'html.parser')
# print(new_soup.prettify())
# print(new_soup.title)
# print(new_soup.title.string)
# print(new_soup.title.name)
# print(new_soup.a) # Anchor Tag
# print(new_soup.p)  # Paragraph Tag
# print(new_soup.li)
# print(new_soup.li.string)

# TODO - findall method
# anchor_tags = new_soup.find_all(name='a')  # results in a list
# print(anchor_tags)
# anc = anchor_tags
# print(anc[1].get('href'))
# for tag in anchor_tags:
#     print(tag.get('href'))

# h1 = new_soup.find_all(name='h1')  # results in a list
# # print(anchor_tags)
# for header in h1:
#     print(header.getText())

# h3 = new_soup.find_all(name='h3', class_='heading')  # results in a list
# # print(anchor_tags)
# for header in h3:
#     print(header.getText())

appmillers_url = new_soup.select_one(selector='p a')
print(appmillers_url.get('href'))

# tag = new_soup.select_one(selector='#name')
# print(tag.getText())

# tag = new_soup.select(selector='.heading')
# print(tag)
