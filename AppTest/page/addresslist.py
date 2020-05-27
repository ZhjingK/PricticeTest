from appium.webdriver.common.mobileby import MobileBy

from AppTest.page.basepage import BasePage
from AppTest.page.member_invite import MemberInvite


class AddressList(BasePage):
    def add_member(self):
        self.find(MobileBy.XPATH, '//*[@text="添加成员"]').click()

        return MemberInvite(self._driver)
