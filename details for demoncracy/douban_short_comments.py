import selenium.webdriver
import time
import pickle
import random
import pandas
from selenium import webdriver


class DoubanImg():
    def __init__(self, broadcast_url):
        self.douban = "https://douban.com"
        self.account = "17720509401"
        self.password = "FP5-xyN-oUG-Nf7"
        self.browser = webdriver.Chrome()
        self.broadcast_url = broadcast_url

    def login_douban(self):
        #使用chrome的webdriver
        #開啟douban首页
        self.browser.get(self.douban)
        self.browser.switch_to.frame(
            self.browser.find_element_by_tag_name("iframe"))
        self.browser.find_element_by_class_name("account-tab-account").click()
        self.browser.find_element_by_id("username").send_keys(self.account)
        self.browser.find_element_by_id("password").send_keys(self.password)
        self.browser.find_element_by_class_name(
            "account-form-field-submit ").click()
        self.browser.switch_to.default_content()

    def img_url_get(self, page):
        res = []
        if page == 1:
            self.browser.execute_script(
                f"window.location.href=\"{self.broadcast_url}\";")
        else:
            self.browser.execute_script(
                f"window.location.href=\"{self.broadcast_url}?p={page}\";")

        for i in self.browser.find_elements_by_class_name("view-large"):
            res.append(i.get_attribute("href"))
            time.sleep(random.random())

        return res

    def img_url_get_multi_pages(self, begin_page_number, end_page_number):
        res = []
        for page in range(begin_page_number, end_page_number):
            res.append(self.img_url_get(page))
            time.sleep(random.random())

        self.browser.close()
        return res


def file_writen(file_name, res):
    img_file = open(file_name, "w")
    for page in res:
        for img_url in page:
            img_file.write(img_url + "\n")

    img_file.close()


if __name__ == "__main__":
    broadcast_url = "https://www.douban.com/people/luwanweizhuang/statuses"
    broadcast_noexistsnake = "https://www.douban.com/people/XIAOHUA4709/statuses"
    begin = 100
    end = 117
    file_name = "img_urls_100-120.txt"
    douban_img_obj = DoubanImg(broadcast_url)
    #douban_img_obj2 = DoubanImg(broadcast_noexistsnake)
    douban_img_obj.login_douban()
    time.sleep(3)
    res = douban_img_obj.img_url_get_multi_pages(begin, end)
    file_writen(file_name, res)
