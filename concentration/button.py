# -*- coding: utf-8 -*-

import tkinter as tk
import random

w = None
w2 = None
imgs = []

# クリックイベント
def btn_click(event):
    global w, w2
    if w2 != None: # 裏返り待ち
        return
    if event.widget.cget('image') != str(imgs[25]): # 裏返り済み
        print(event.widget.cget('image'))
        return

    no = int(event.widget["text"])
    event.widget.config(image=imgs[no])
    if w == None: # 1枚目
        w = event.widget
        return
    else: # 2枚目
        s = int(event.widget["text"]) % 13
        n = int(w["text"]) % 13
        if s != n:
            w2 = event.widget
            win.after(2000, timer)
        else: # 一致
            w = None

# タイマー
def timer():
    global w, w2
    if w2 != None:
        w.config(image=imgs[52])
        w2.config(image=imgs[52])
        w = None
        w2 = None

# ニューゲーム
def new_game():
    global w, w2
    w = None
    w2 = None

    # かき混ぜ
    for i in range(100):
        n = random.randint(0, 51)
        s = random.randint(0, 51)
        t = nums[n]
        nums[n] = nums[s]
        nums[s] = t
    children = win.winfo_children()
    for child in children:
        if child["text"] != "new game":
            child.confing(image=imgs[52])

win = tk.Tk()

# メインウィンドウを作成
win.geometry("900x420")
win.title("神経衰弱")

# イメージ作成
for i in range(1, 14):
    mstr = "concentration/asset/card_club_" + str(i).zfill(2) + ".png"
    img = tk.PhotoImage(file=mstr, width=409, height=600)
    img = img.subsample(6, 6)
    imgs.append(img)
for i in range(1, 14):
    mstr = "concentration/asset/card_diamond_" + str(i).zfill(2) + ".png"
    img = tk.PhotoImage(file=mstr, width=409, height=600)
    img = img.subsample(6, 6)
    imgs.append(img)
for i in range(1, 14):
    mstr = "concentration/asset/card_heart_" + str(i).zfill(2) + ".png"
    img = tk.PhotoImage(file=mstr, width=409, height=600)
    img = img.subsample(6, 6)
    imgs.append(img)
for i in range(1, 14):
    mstr = "concentration/asset/card_spade_" + str(i).zfill(2) + ".png"
    img = tk.PhotoImage(file=mstr, width=409, height=600)
    img = img.subsample(6, 6)
    imgs.append(img)

img = tk.PhotoImage(file="concentration/asset/card_back.png", width=409, height=600)
img = img.subsample(6, 6)
imgs.append(img)

# 番号
nums = []
for i in range(52):
    nums.append(i)

new_game()

# ボタン配置
ii = 0
for j in range(4):
    for i in range(13):
        # ボタンの数字
        button_name = ii
        # ボタンのnew
        button = tk.Button(
            win,
            text=nums[button_name],
            width=62,
            height=92,
            bg="#ffffff",
            image=imgs[52],
        )
        ii = ii + 1
        # ボタンの配置
        button.grid(column=i, row=j+1)
        button.bind("<ButtonPress>", btn_click)
tk.Button(win, text="new game", command=new_game).grid(column=0, row=0)
win.mainloop()
