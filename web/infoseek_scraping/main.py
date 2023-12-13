import requests
import bs4

url = 'https://www.infoseek.co.jp/'

req = requests.get(url) # 指定したURLのページを取得
data = bs4.BeautifulSoup(req.content, 'html.parser')# 複雑なHTMLを解析
index = data.find('ul', 'topics-mini-list') # <div class="newsFeed_list">を取得
list_text = index.getText() # テキストのみに変換
print(list_text)

file = open('infoseek_news.test', 'w')
file.write(list_text)
file.close()
