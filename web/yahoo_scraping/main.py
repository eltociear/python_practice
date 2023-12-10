import requests
import bs4

url = 'https://news.yahoo.co.jp/'

req = requests.get(url) # 指定したURLのページを取得
data = bs4.BeautifulSoup(req.content, 'html.parser')# 複雑なHTMLを解析
index = data.find('div', 'newsFeed_list') # <div class="newsFeed_list">を取得
print(index)
# list_text = index.getText() # テキストのみに変換

file = open('yahoo_news.txt', 'w')
# file.write(list_text)
file.close()
