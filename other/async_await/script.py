import asyncio
import time

async def function_1(sec):
    print(f"{sec}秒待ちます")
    await asyncio.sleep(sec)
    return f"{sec}秒の待機に成功しました"

async def main(): # async defでコルーチン(処理をある場所で一時中断・再開できる)を定義
    print(f"main開始 {time.strftime('%X')}")
    task1 = asyncio.create_task(function_1(1)) # create_task()で子ルーチンをラップしたタスクを作成 -> これで並行処理が可能
    results = await asyncio.gather(function_1(2), task1) # gather()の引数にtaskやコルーチンを渡すと、並行処理が可能(コルーチンは自動的にタスクにラップされる)
    print(results) # gather()の戻り値はタスクの実行結果をリストにまとめたもの
    print(f"main終了 {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main()) # asyncio.run()はイベントループを作り、引数のコルーチンを実行
