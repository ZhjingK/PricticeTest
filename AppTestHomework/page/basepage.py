'''
作业：
PO模式实现 企业微信添加联系人、删除联系人

要求：
添加多条联系人，利用参数化，数据驱动
封装find方法处理异常弹框
'''
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _black_list = [
        (By.XPATH, '//*[@text="确认"]'),
        (By.XPATH, '//*[@text="下次再说"]'),
        (By.XPATH, '//*[@text="确定"]'),
    ]

    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        try:
            if isinstance(locator, tuple):
                element: WebElement = self._driver.find_element(*locator)
            else:
                element: WebElement = self._driver.find_element(locator, value)

            self._error_num = 0
            self._driver.implicitly_wait(5)

            return element
        except Exception as e:
            self._driver.implicitly_wait(1)

            if self._error_num > self._max_num:
                raise e

            self._error_num += 1

            for black in self._black_list:
                ele = self._driver.find_elements(*black)
                if len(ele) > 0:
                    ele[0].click()

                    return self.find(locator, value)

