from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pickle

# 設定 ChromeDriver 路徑
# chrome_driver_path = '/path/to/chromedriver'  # 替換為你的 ChromeDriver 路徑
profile_path = "C:\\Users\\water\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
# 設定 Chrome 選項
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={profile_path}")
chrome_options.add_argument('--disable-gpu')  # 如果你使用的是 Windows，這一步是必要
# 創建 WebDriver
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    # 導航到 Google 網站
    driver.get('https://w3.cathaylife.com.tw/eai/ZPWeb/login.jsp')
    time.sleep(3)

    # 找到帳號輸入框並輸入帳號
    username_input = driver.find_element(By.XPATH, '//*[@id="UID"]')  # 確保替換為實際的 input 標籤名稱或 ID
    username_input.send_keys('00897554')  # 替換為實際的帳號
    # 找到密碼輸入框並輸入密碼
    password_input = driver.find_element(By.XPATH, '//*[@id="KEY"]')  # 確保替換為實際的 input 標籤名稱或 ID
    password_value = "#K880322"  # 替換為實際的密碼
    driver.execute_script("arguments[0].value = arguments[1];", password_input, password_value)
    time.sleep(3)
    # 找到登錄按鈕並點擊
    login_button = driver.find_element(By.XPATH, '//*[@id="btnLogin"]')  # 確保替換為實際的按鈕 XPATH 或 ID
    login_button.click()
    # 等待登錄完成並跳轉頁面
    time.sleep(10)
    # 打卡按鈕點擊
    check_button = driver.find_element(By.XPATH, '//*[@id="checkinBtn"]')
    check_button.click()
    time.sleep(10)

finally:
    # 關閉瀏覽器
    time.sleep(10)
    driver.quit()


