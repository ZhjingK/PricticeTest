'''
App首页
'''
from appium.webdriver.common.mobileby import MobileBy

from AppTest.page.addresslist import AddressList
from AppTest.page.basepage import BasePage


class Main(BasePage):
    def goto_message(self):
        pass

    def goto_addresslist(self):
        self.find(MobileBy.XPATH, '//*[@text="通讯录" and @resource-id="com.tencent.wework:id/drk"]').click()
        return AddressList(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass
