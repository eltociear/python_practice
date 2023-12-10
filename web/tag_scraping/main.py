# -*- coding: utf-8 -*-

# ライブラリのインポート
import requests
from bs4 import BeautifulSoup
from time import sleep # スクレイピングのタイミングを制御する（サーバに負荷をかけないため）

target_tag = 'title' # 取得したいタグを指定

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
            article1_content = soup.find_all(target_tag) # タグを指定して取得
            temp = []
            for con in article1_content:
                out = con.text
                temp.append(out)
            text = ''.join(temp)
            all_text.append(text)
            sleep(1)
        return all_text

    # 配列の中身をインデックス付きの文字列に変換
    def convert_text(self, text):
        temp = []
        for i, t in enumerate(text):
            temp.append(str(i + 1) + ': ' + t)
            # 改行コードを入れる
            temp.append('\n\n')
        return ''.join(temp)

# URL指定
sc = Scraping(['https://toukei-lab.com/conjoint', 'https://toukei-lab.com/correspondence'])
text_list = sc.get_url()
print(sc.convert_text(text_list))
