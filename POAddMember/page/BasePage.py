from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


# 子类在执行之前先去实例化父类，调用父类的构造方法
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 类变量(需要在函数之前对其进行赋值)
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            option.add_experimental_option('w3c', False)
            self._driver = webdriver.Chrome(options=option)
            self._driver.maximize_window()
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_for_click(self, locator, time = 10):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

