from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Edge WebDriverを起動
browser = webdriver.Edge()

# Webページを開く
browser.get("https://ssl.jobcan.jp/login/mb-employee?client_id=nex0729&lang_code=ja")

# 検索ボックスを特定し、キーワードを入力
mail_box = browser.find_element(By.NAME, "email")
mail_box.send_keys("メールアドレス")

password_box = browser.find_element(By.NAME, "password")
password_box.send_keys("パスワード")

time.sleep(3)  # このsleepは本来は必要ない（デモ用）

# ボタンを特定してクリック（CLASS_NAMEを用いた例）
button = browser.find_element(By.CLASS_NAME, 'btn-info')  
button.click()

# もしくはCSSセレクタを使用してもよい
# button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-info.btn-block')
# button.click()

time.sleep(5)  # このsleepは本来は必要ない（デモ用）

button2=browser.find_element(By.XPATH,'//*[@id="container"]/div[7]/h3')
button2.click()
time.sleep(3)

button3 = browser.find_element(By.LINK_TEXT,"修正申請")
button3.click()
time.sleep(3)

kintai_input=browser.find_element(By.XPATH,'//*[@id="container"]/div[4]/table/tbody/tr[2]/td/a/li/em')
kintai_input.click()

in_time=browser.find_element(By.NAME,"time1")
in_time.send_keys("始業時間")

out_time=browser.find_element(By.NAME,"time2")
out_time.send_keys("就業時間")

time.sleep(3)

shinsei_button=browser.find_element(By.XPATH,'//*[@id="container"]/div[4]/form/input[6]')
shinsei_button.click()

browser.quit()