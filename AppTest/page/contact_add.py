from appium.webdriver.common.mobileby import MobileBy

from AppTest.page.basepage import BasePage


class ContactAdd(BasePage):
    def input_name(self):
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/au_" and @text="必填"]').send_keys("静")

        return self

    def set_gender(self):
        self.find(MobileBy.XPATH,
                                 '//*[@text="性别"]/..//*[@resource-id="com.tencent.wework:id/av4"]').click()
        self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        return self

    def input_phone(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/er6').send_keys('13678654323')

        return self

    def click_post(self):
        self.find(MobileBy.XPATH,
                                 '//*[@resource-id="com.tencent.wework:id/av4" and @text="设置部门"]').click()
        self.find(MobileBy.ID, 'com.tencent.wework:id/fny').click()
        return self

    def click_save(self):
        # 出现循环调用，导入包的时候需要【局部导入】
        from AppTest.page.member_invite import MemberInvite

        self.find(MobileBy.ID, 'com.tencent.wework:id/gvy').click()

        return MemberInvite(self._driver)
