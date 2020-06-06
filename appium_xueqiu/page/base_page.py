import inspect
import json

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from appium_xueqiu.page.wrapper import handle_black


class BasePage:

    _parame = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def finds(self, locator, value: str = None):
        elements:list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)

        return elements

    @handle_black
    def find(self, locator, value: str = None):
        element:WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)

        return element

    @handle_black
    def find_get_text(self, locator, value: str = None):
        if isinstance(locator, tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text

        return element_text

    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            # inspect获取当前运行的函数名
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]

        raw = json.dumps(steps)
        # 利用json的replace方法进行字符串替换
        for key, value in self._parame.items():
            raw = raw.replace(f'${{{key}}}', value)
        steps = json.loads(raw)

        for step in steps:
            if 'action' in step.keys():
                action = step['action']
                if 'click' == action:
                    self.find(step['by'], step['locator']).click()
                if 'send' == action:
                    self.find(step['by'], step['locator']).send_keys(step['value'])
                if 'len>0' == action:
                    elements = self._driver.find_elements(step['by'], step['locator'])
                    return len(elements) > 0

