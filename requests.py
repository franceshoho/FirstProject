import requests

from bs4 import BeautifulSoup

# to get hyper link of act3 of

act = 3
link = 'http://www.gutenberg.org/files/3825/3825-h/3825-h.htm'
r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')
a_tags = soup.find_all('a')
act3_tag = a_tags[act - 1]
print(act3_tag['href'])