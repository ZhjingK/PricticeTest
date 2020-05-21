from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver


class Register():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="corp_name"]').send_keys("hello")
        self.driver.find_element_by_xpath('//*[@id="manager_name"]').send_keys("zj")
        self.driver.quit()
        return True


