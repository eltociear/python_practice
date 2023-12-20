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

func_hi()
func_bye()
