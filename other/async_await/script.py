import asyncio
import time

async def function_1(sec):
    print(f"{sec}秒待ちます")
    await asyncio.sleep(sec) # asyncio.sleep()はawaitで待機可能なコルーチン。time.sleep()とは違い、イベントループによって非同期に実行される
    return f"{sec}秒の待機に成功しました"

async def main(): # async defでコルーチン(処理をある場所で一時中断・再開できる)を定義
    print(f"main開始 {time.strftime('%X')}")
    result_1 = await function_1(1)
    result_2 = await function_1(2)
    print(result_1)
    print(result_2)
    print(f"main終了 {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main()) # asyncio.run()はイベントループを作り、引数のコルーチンを実行
