from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.yahoo.co.jp/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

for elem in elems:
    print(elem.text) # または elem.string を使用
    print(elem.get('href')) # リンク先を取得
