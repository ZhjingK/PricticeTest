from selenium import webdriver

from seleniumPO.login import Login
from seleniumPO.register import Register


class Index():
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        self._driver.find_element_by_xpath('//*[@class="index_top_operation_loginBtn"]').click()
        return Login(self._driver)

    def goto_register(self):
        # 点击注册
        self._driver.find_element_by_xpath('//*[@class="index_head_info_pCDownloadBtn"]').click()
        return Register(self._driver)
