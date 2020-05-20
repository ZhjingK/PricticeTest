import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db = shelve.open("cookies")
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(3)
        db.close()
