from threading import Thread
import time
import sys

def func_hi():
    for _ in range(100):
        print('hi', end='')
        sys.stdout.flush() # print()はstdoutに出力するので、flush()でバッファがフラッシュされて強制的に出力する
        time.sleep(0.2)
    print() # 空文字列を出力することで、改行されないようにする

def func_bye():
    for _ in range(100):
        print('bye', end='')
        sys.stdout.flush() # print()はstdoutに出力するので、flush()でバッファがフラッシュされて強制的に出力する
        time.sleep(0.2)
    print() # 空文字列を出力することで、改行されないようにする

'''
デーモンスレッドを使わない場合は以下
'''
hi_thread = Thread(target=func_hi)
bye_thread = Thread(target=func_bye)

hi_thread.start() # .start()でスレッドを開始する
bye_thread.start() # .start()でスレッドを開始する

hi_thread.join() # .join()でスレッドの終了を待つ
bye_thread.join() # .join()でスレッドの終了を待つ
print('FINISHED not daemon thread')


'''
デーモンスレッド(main.py)の場合は以下(control+cで終了)
'''
Thread(target=func_hi, daemon=True).start()
Thread(target=func_bye, daemon=True).start()
while True: # メインスレッドが終了しないようにする（無限ループ）
    time.sleep(1) # ビジーループを避けるために1秒スリープする
