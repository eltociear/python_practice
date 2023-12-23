import asyncio
import time

async def main(): # async defでコルーチン(処理をある場所で一時中断・再開できる)を定義
    print(f"main開始 {time.strftime('%X')}")
    await asyncio.sleep(1) # asyncio.sleep()はawaitで待機可能なコルーチン。time.sleep()とは違い、イベントループによって非同期に実行される
    await asyncio.sleep(2)
    print(f"main終了 {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main()) # asyncio.run()はイベントループを作り、引数のコルーチンを実行
