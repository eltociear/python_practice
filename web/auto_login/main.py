from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() # pip3でインストールしている場合、execute_pathを指定する必要はない

user_info = {'username': 'TEST', 'password': 'PASS'}
target_url = 'https://example.com/login'
user_box_name = 'username'
pass_box_name = 'password'
button_type = 'submit'

def main():
    try:
        # URLにアクセス
        driver.get(target_url)
        # ブラウザが開き切るまで待機(seleniumにもwait機能はあるが、今回はtime.sleepで代用)
        time.sleep(2)

        # ユーザー名を入力
        user_box = driver.find_element(by=By.XPATH, value="//input[@name='" + user_box_name + "']")
        user_box.send_keys(user_info['username'])

        # パスワードを入力
        pass_box = driver.find_element(by=By.XPATH, value="//input[@name='" + pass_box_name + "']")
        pass_box.send_keys(user_info['password'])
        pass_box.send_keys(Keys.ENTER) # パスワードは入力のみだとログインできない場合があるので、ENTERキーを送信

        # ログインボタンをクリック
        login_btn = driver.find_element(by=By.XPATH, value="//button[@type='" + button_type + "']")
        login_btn.click()
    except Exception as e:
        print(e)
    finally:
        input("Press Enter to close...")
        driver.quit()

if __name__ == "__main__":
    main()
