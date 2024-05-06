import time
import pickle
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.douban.com")
time.sleep(20)
cookie = driver.get_cookies()
print(cookie)
pickle.dump(cookie, open("cookies.pkl", "wb"))
