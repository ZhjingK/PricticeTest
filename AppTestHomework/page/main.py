from appium.webdriver.common.mobileby import MobileBy

from AppTestHomework.page.addmember import AddMember
from AppTestHomework.page.basepage import BasePage


class Main(BasePage):
    def goto_list(self):
        # 点击通讯录
        # self._driver.find_element(MobileBy.XPATH, '//*[@text="通讯录" and @resource-id="com.tencent.wework:id/drk"]').click()
        self.find(MobileBy.XPATH, '//*[@text="通讯录" and @resource-id="com.tencent.wework:id/drk"]').click()
        return AddMember(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass

