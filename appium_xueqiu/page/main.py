
from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self._driver.implicitly_wait(10)
        self.steps('../page/main.yaml')
        self._driver.implicitly_wait(3)
        return Market(self._driver)

