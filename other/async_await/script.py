import asyncio
import time

async def function_1(sec):
    print(f"{sec}秒待ちます")
    await asyncio.sleep(sec)
    return f"{sec}秒の待機に成功しました"

async def main(): # async defでコルーチン(処理をある場所で一時中断・再開できる)を定義
    print(f"main開始 {time.strftime('%X')}")
    try:
        results = await asyncio.wait_for(function_1(10), timeout = 5) # asyncio.wait_for()でコルーチンの実行を待つ、timeoutでタイムアウト時間を指定
        print(results)
    except asyncio.TimeoutError:
        print("タイムアウトしました")
    print(f"main終了 {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main()) # asyncio.run()はイベントループを作り、引数のコルーチンを実行
