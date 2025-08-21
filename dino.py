# PILLow, numpy
import base64
import time
import numpy as np
import os

# 拿到目前的圖片存在這裡
dn = "record"
if not os.path.exists(dn):
    os.makedirs(dn)

from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# 如果不做設置, chrome視窗有可能會自動關閉
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options,
                          service=Service(ChromeDriverManager().install()))

# 命令瀏覽器瀏覽這個網站
driver.get("https://chromedino.com/")
# 把視窗最大化
driver.maximize_window()

# 休息三秒等待網頁讀完
time.sleep(3)
# F12->方塊滑鼠會找到小恐龍區塊叫做canvas
canvas = driver.find_element(By.TAG_NAME, "canvas")

# 送出第一個空白鍵(才會開始遊戲)
actions = ActionChains(driver)
actions.send_keys(Keys.SPACE)
actions.perform()

# 無窮迴圈(條件永遠是對的)
while True:
    # 0.01秒做一次判斷
    time.sleep(0.01)
    # (!!!JavaScript網頁語法) 請求剛剛的canvas把現在狀態轉成png給我
    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
    # (不用在意) 圖片編碼BASE64(A-Z a-z 0-9)
    canvas_png = base64.b64decode(canvas_base64)
    # 準備我寫入入境 record/canvas.png裡
    fn = dn + "/canvas.png"
    # 把目前圖片寫入 w(字串) -> wb(原始01)
    f = open(fn, 'wb')
    f.write(canvas_png)
    f.close()

    # 檢查到底要不要跳:
    # 把剛剛圖片打開 預設彩色圖片(RGBA) convert("L")->灰階圖片(0:白, 255:黑)
    img = Image.open(fn).convert("L")
    img_np = np.array(img)

    # 圖片高度: 150px, 恐龍手位置大概: 下面屬上來30px
    # 圖片寬度: 600px, 檢查範圍 60px-120px 太近:恐龍本題 太遠: 太早跳
    # range(60, 120) -> [60, 61, ...., 119]
    # 座標(-30, 60) -> (-30, 120) 看一下有沒有黑色霧
    for i in range(60, 90):
        # > 50 隨便填的, 灰色
        if img_np[-30][i] > 50:
            print("jump")
            actions = ActionChains(driver)
            actions.send_keys(Keys.SPACE)
            actions.perform()
            break