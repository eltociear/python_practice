from threading import Thread

def worker():
    print('Hi')

# targetに関数、daemon=Trueでデーモンスレッドになる（True:メインスレッド終了時に勝手に破棄される）
Thread(target=worker, daemon=True).start() # .start()でスレッドを開始する
