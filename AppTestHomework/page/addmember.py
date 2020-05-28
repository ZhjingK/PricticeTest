from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from AppTestHomework.page.ManageContacts import ManageContacts
from AppTestHomework.page.basepage import BasePage
from AppTestHomework.page.invitemember import InviteMember


class AddMember(BasePage):
    def addmember(self):
        # 点击添加成员
        # self._driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()

        # self.find(MobileBy.XPATH, '//*[@text="添加成员"]').click()

        # 成员众多的时候需要滑动定位
        self._driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()

        return InviteMember(self._driver)

    def manage_contacts(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/gvw').click()
        return ManageContacts(self._driver)
