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

from AppTestHomework.page.wrapper import handler_black


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

    def finds(self, locator, value: str = None):
        if isinstance(locator, tuple):
            elements: list = self._driver.find_elements(*locator)
        else:
            elements: list = self._driver.find_elements(locator, value)
        return elements

    @handler_black
    def find(self, locator, value):
        if isinstance(locator, tuple):
            element: WebElement = self._driver.find_element(*locator)
        else:
            element: WebElement = self._driver.find_element(locator, value)

        return element

    @property
    def driver(self):
        return self._driver

