# -*- coding: utf-8 -*-
# ↑日本語を使うためのおまじない

import tkinter as tk #PythonでGUIを作成するための標準ライブラリ
import random        #乱数を生成するためのライブラリ

check=[1,4],[0,2,5],[1,3,6],[2,7],[0,5,8],[1,4,6,9],[2,5,7,10],[3,6,11],[4,9,12],[5,8,10,13],[6,9,11,14],[7,10,15],[8,13],[9,12,14],[10,13,15],[11,14]
#ボタンリスト ボタンを格納し、表示している数字を変えたり、どれが押されたかを判定するために使う
buttons=[]
#空ボタン
kara=15

#かき混ぜ 最初とクリア後の再プレイで呼び出す
def maze():
    global kara
    for i in range(100): #100回くらいかき混ぜる
        n=random.randint(0, 15) #0から15の乱数を生成
        for itm in check[n]:
            if itm==kara:
                buttons[kara]["text"]=buttons[n]["text"]
                buttons[n]["text"]=""
                kara=n

#ボタン押したら呼び出す
def button_func(event):
    global kara
    if event.widget.cget("text")=="clear": #クリアのボタンを押すと再プレイ用にかき混ぜる
        maze()
        return

    n=0
    for item in buttons:
        if event.widget==item:
            break
        else:
            n=n+1
    for itm in check[n]:
        if item==kara:
            buttons[kara]["text"]=event.widget.cget("text")
            buttons[n]["text"]=""
            kara=n

#クリアチェック
def clear_chk():
    n=0
    for item in buttons:
        n=n+1
        if n != item["text"]:
            break
    if n==16 and item["text"]=="":
        item["text"]="clear"
        #win.title("clear")
    win.after(1000, clear_chk) #1秒ごとに自分を呼び出してクリアチェック

win=tk.Tk() #このTKでウィンドウ作成

### ↓画面作ったりボタン配置したり
#ボタン配置
for j in range(4):
    for i in range(4): #4*4=16のボタンを配置
        #ボタンの数字
        button_name = 4*j+i+1 #ボタンに表示する数字（0からでなく1から始めるため+1）
        if button_name==16:
            button_name="" #16は空白にする
        #ボタンのnew
        button = tk.Button(win, text=button_name, width=10, height=5, bg='#ffffcc', font=("", 20))
        #ボタンの配置
        button.grid(row=j, column=i)
        #ボタンクリックイベント登録
        button.bind("<ButtonPress>", button_func)
        buttons.append(button) #ボタンオブジェクトを配列に追加
maze() #画面ができたらかき混ぜる
win.after(1000, clear_chk)
win.title("16 ゲーム")
#メインループ実行
win.mainloop()
