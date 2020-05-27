from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

import logging


class BasePage:
    logging.basicConfig(level=logging.INFO)
    # 弹框处理的名单
    _black_ist = [
        (By.XPATH, '//*[@text="确认"]'),
        (By.XPATH, '//*[@text="下次再说"]'),
        (By.XPATH, '//*[@text="确定"]'),
    ]

    # 最大查找次数设置为三次
    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value: str = None):
        '''
        查找元素的时候弹框处理
        :param locator:
        :param value:
        :return:
        '''

        logging.info(locator)
        logging.info(value)

        try:
            element: WebElement = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)

            # if isinstance(locator, tuple):
            #     element: WebElement = self._driver.find_element(*locator)
            # else:
            #     element: WebElement = self._driver.find_element(locator, value)

            # 找到元素之后，_error_num归零
            self._error_num = 0

            # 元素查找完之后，再将隐式等待设置为10秒
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            '''
            处理弹框导致的没有找到元素的情况,最大查找次数为三次
            做法：点击弹框、查找元素
            '''
            # 查找元素出现异常的时候将隐式等待设置成1秒，快速的处理弹框
            self._driver.implicitly_wait(1)

            # 判断异常处理次数
            if self._error_num > self._max_num:
                raise e

            self._error_num += 1

            # 处理弹框
            for ele in self._black_ist:
                logging.info(ele)
                ele_list = self._driver.find_elements(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    # 处理玩弹框之后，去查找目标元素
                    return self.find(locator, value)

            raise e

    def find_and_gettext(self, locator, value: str = None):
        '''
        查找元素并获取text属性时弹框处理
        :param locator:
        :param value:
        :return:
        '''
        try:
            text = self._driver.find_element(*locator).text if isinstance(locator, tuple) else self._driver.find_element(locator, value).text

            self._error_num = 0

            self._driver.implicitly_wait(10)
            return text
        except Exception as e:
            self._driver.implicitly_wait(1)

            if self._error_num > self._max_num:
                raise e

            self._error_num += 1

            for ele in self._black_ist:
                ele_list = self._driver.find_elements(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return self.find(locator, value).text

            raise e
