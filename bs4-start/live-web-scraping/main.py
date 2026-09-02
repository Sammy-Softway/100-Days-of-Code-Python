from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# print(response.status_code)
# print(response.text)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
# print(soup.prettify())

# target_act = soup.find(name="span", class_="titleline")
# target_text = target_act.get_text()
# target_link = target_act.a.get('href')
# print(target_text)
# print(target_link)
# target_upvote = soup.find(name="span", class_="score")
# print(target_upvote)
# print(target_upvote.text)

target_texts = []
target_links = []

target = soup.find_all(name="span", class_="titleline")
for act in target:
    text = act.get_text()
    target_texts.append(text)
    link = act.a.get('href')
    target_links.append(link)
print(target_texts)
print(target_links)

target_upvote = [score.get_text() for score in soup.find_all(name="span", class_="score")]
target_upvote_int = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(target_upvote)
print(target_upvote_int)


highest_upvote = max(target_upvote_int)

highest_upvote_index = target_upvote_int.index(highest_upvote)

print(f"Text: {target_texts[highest_upvote_index]}\n"
      f"Link: {target_links[highest_upvote_index]}\n"
      f"Upvotes: {target_upvote[highest_upvote_index]}")