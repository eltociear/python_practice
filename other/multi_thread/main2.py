def func_hi():
    for _ in range(100):
        print('hi', end='')
    print() # 空文字列を出力することで、改行されないようにする

def func_bye():
    for _ in range(100):
        print('bye', end='')
    print() # 空文字列を出力することで、改行されないようにする

func_hi()
func_bye()
