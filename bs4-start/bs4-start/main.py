from bs4 import BeautifulSoup

with open("website.html") as file:
    website = file.read()
    # print(website)

soup = BeautifulSoup(website, 'html.parser')

# print(soup)
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

#-----Gets only the first element of the request made, e.g as seen below-----#
# print(soup.p)
# print(soup.a)

#-----Gets all elements of the request made, e.g as seen below-----#
all_anchors = soup.find_all(name='a')
all_paragraphs = soup.find_all(name='p')
# print(all_anchors)
# print(all_paragraphs)

# for anchor in all_anchors:
    # print(anchor.text)
    # print(anchor['href'])
    # print(anchor.get('href'))  #Both executes the same way

# for paragraph in all_paragraphs:
#     print(paragraph.getText())

header = soup.find(name='h1', id='name')
# print(header.text)

specific_header = soup.find(name='h3', class_='heading')
# print(specific_header.text)

selected_url = soup.select_one(selector='p a')
# print(selected_url)
# print(selected_url.text)
# print(selected_url['href'])

name = soup.select_one(selector='#name')
print(name)

headings = soup.select(selector='.heading')
print(headings)

for heading_words in headings:
    print(heading_words.text)