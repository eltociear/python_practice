# -*- coding: utf-8 -*-

# ライブラリのインポート
import requests
from bs4 import BeautifulSoup
from time import sleep # スクレイピングのタイミングを制御する（サーバに負荷をかけないため）

# スクレイピング
# URLを配列に格納してわたすと、<p>に入っているテキストを取得して配列に格納して返す
class Scraping():
    def __init__(self, urls):
        self.urls = urls

    def get_url(self):
        all_text = []
        for url in self.urls:
            res = requests.get(url) # URLにアクセス
            content = res.content
            soup = BeautifulSoup(content, 'html.parser')
            article1_content = soup.find_all('p') # タグを指定して取得（今回は<p>を全て取得）
            temp = []
            for con in article1_content:
                out = con.text
                temp.append(out)
            text = ''.join(temp)
            all_text.append(text)
            sleep(1)
        return all_text
sc = Scraping(['https://toukei-lab.com/conjoint', 'https://toukei-lab.com/correspondence'])
print(sc.get_url())
