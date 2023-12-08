import tkinter as tk
from tkinter import font # 文字を書くために必要
import random
# import winsound # Windowsのみの音楽再生ライブラリ

global xp, yp # プレイヤーの座標
dp = 0 # 向いている方向
hp = 300
mp = 300
zFlg = 0
cFlg = 0
pFlg = 0
counter = 0

class Maze:
    def make(self):
        maze = [[0 for i in range(26)] for j in range(26)]
        wall = [-1, 0, 1, 0, -1] # 配列を初期化
        for x in range(25):
            # 迷路の外周を壁にする
            maze[x][0] = 1
            maze[x][24] = 1
            maze[24][x] = 1
            maze[0][x] = 1

        for x in range(2, 24, 2):
            for y in range(2, 24, 2):
                maze[x][y] = 1
                while True:
                    direction = 0
                    if y == 2:
                        direction = random.randint(0, 3)
                    else:
                        direction = random.randint(0, 2)
                    wallX = x + wall[direction]
                    wallY = y + wall[direction + 1]
                    if maze[wallX][wallY] != 1:
                        maze[wallX][wallY] = 1
                        break
            return maze

global map
mapf = [[1 for i in range(26)] for j in range(26)]
window = tk.Tk()
# メインウィンドウを作成
window.geometry("950x950") # ウィンドウのサイズを設定
window.title("3Dダンジョン") # ウィンドウのタイトルを設定
window.configure(bg="#c3c3c3", height=600, width=900) # ウィンドウの背景色を設定
# キャンバス作成
canvas = tk.Canvas(window, width=900, height=600, bg="#c3c3c3")
# キャンバスを配置
canvas.place(x=10, y=30)
zimage = tk.PhotoImage(file="z.png")
cimage = tk.PhotoImage(file="c.png")
cimage = cimage.subsample(4)
pimage = tk.PhotoImage(file="p.png")
pimage = pimage.subsample(5)
# キャンバスに画像を表示

gameoverFlg = 0

def keyPress(ev):
    global xp, yp, dp, map, hp, mp, zFlg, cFlg, pFlg, counter
    pFlg = 0
    cFlg = 0
    zFlg = 0
    mapf[xp][yp] = 0
    if ev.keysym == 'Right':
        dp = dp - 1
    if ev.keysym == 'Left':
        dp = dp + 1
    if ev.keysym == 'Up':
        if dp == 0 and map[xp + 1][yp] == 0:
            xp = xp + 1
        if dp == 1 and map[xp][yp - 1] == 0:
            yp = yp - 1
        if dp == 2 and map[xp - 1][yp] == 0:
            xp = xp - 1
        if dp == 3 and map[xp][yp + 1] == 0:
            yp = yp + 1
    if ev.keysym == 'Down': # TODO: 以下要確認
        if dp == 0 and map[xp - 1][yp] == 0:
            xp = xp - 1
        if dp == 1 and map[xp][yp + 1] == 0:
            yp = yp + 1
        if dp == 2 and map[xp + 1][yp] == 0:
            xp = xp + 1
        if dp == 3 and map[xp][yp - 1] == 0:
            yp = yp - 1

    mapf[xp][yp] = 0 # 移動した位置を覆っていた黒を消す
    counter = counter + 1
    at = random.randint(0, 50) # 5分の1の確率で敵が出現

    if at > 45: # 敵が出現した場合
        canvas.unbind("<Key>") # キー入力を無効化
        window.bind("<Key>", keyPress2) # キー入力を有効化(移動時と戦闘時でキー入力を分けるため、unbindとbindを使う)
        textBox1.delete(0., tk.END)
        textBox1.insert(tk.END, "敵が現れた！\n")
        # window.bell() # Windowsのみの音楽再生ライブラリ
        zFlg = 1
        e = random.randint(0, 1)
        if e == 0:
            textBox1.delete(0., tk.END)
            textBox1.insert(tk.END, "敵の攻撃！\n")
            e = random.randint(0, 5)
            hp = hp - e
            textBox1.insert(tk.END, str(e)"のマイナス！\n")
        textBox1.insert(tk.END, "1:戦う 2: 魔法 3: 逃げる\n")
    if at == 1: # ケーキが出現した場合
        textBox1.delete(0., tk.END)
        textBox1.insert(tk.END, "ケーキを見つけた！\n")
        hp = hp + 20
        if hp > 350:
            hp = 350
            # winsound.Beep(100, 500)
        cFlg = 1
    if at == 2: # ポーションが出現した場合
        textBox1.delete(0., tk.END)
        textBox1.insert(tk.END, "ポーションを見つけた！\n")
        mp = mp + 20
        if mp > 350:
            mp = 350
            # winsound.Beep(100, 500)
        pFlg = 1
    dp = dp % 4 # 4で割って割り出すので方向を0~3に収める
    window.title(str(dp))
    drawmap() # 書き換え

counter = 0


