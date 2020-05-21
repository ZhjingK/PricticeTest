from selenium.webdriver.remote.webdriver import WebDriver

from seleniumPO.register import Register


class Login():
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def scanf(self):
        pass

    def goto_register(self):
        # 点击立即注册
        self._driver.find_element_by_xpath('//*[@class="login_registerBar_link"]').click()
        return Register(self._driver)