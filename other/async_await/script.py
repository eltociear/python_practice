import asyncio
import time

async def main(): # async defでコルーチン(処理をある場所で一時中断・再開できる)を定義
    print(f"main開始 {time.strftime('%X')}")
    task1 = asyncio.create_task(asyncio.sleep(1)) # create_task()で子ルーチンをラップしたタスクを作成 -> これで並行処理が可能
    task2 = asyncio.create_task(asyncio.sleep(2))
    await task1 # awaitでタスクが完了するまで待機
    await task2
    print(f"main終了 {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main()) # asyncio.run()はイベントループを作り、引数のコルーチンを実行
