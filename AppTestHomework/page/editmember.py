from appium.webdriver.common.mobileby import MobileBy

from AppTestHomework.page.basepage import BasePage
from AppTestHomework.page.invitemember import InviteMember


class EditMember(BasePage):
    # def editinfo(self, name, gender, number):
    #     # 姓名 # 性别 # 电话 # 部门 # 保存 # 断言
    #     self._driver.find_element(MobileBy.XPATH,
    #                              '//*[@resource-id="com.tencent.wework:id/au_" and @text="必填"]').send_keys(name)
    #
    #     # 更改性别为 女
    #     if gender is '女':
    #         self._driver.find_element(MobileBy.XPATH,
    #                              '//*[@text="性别"]/..//*[@resource-id="com.tencent.wework:id/av4"]').click()
    #         self._driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
    #
    #     self._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/er6').send_keys(number)
    #
    #     self._driver.find_element(MobileBy.XPATH,
    #                              '//*[@resource-id="com.tencent.wework:id/av4" and @text="设置部门"]').click()
    #     self._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fny').click()
    #     self._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gvy').click()
    #
    #     return InviteMember(self._driver)
    def editinfo(self, name, gender, number):
        # 姓名 # 性别 # 电话 # 部门 # 保存 # 断言
        self.find(MobileBy.XPATH,
                                 '//*[@resource-id="com.tencent.wework:id/au_" and @text="必填"]').send_keys(name)

        # 更改性别为 女
        if gender is '女':
            self.find(MobileBy.XPATH,
                                 '//*[@text="性别"]/..//*[@resource-id="com.tencent.wework:id/av4"]').click()
            self.find(MobileBy.XPATH, '//*[@text="女"]').click()

        self.find(MobileBy.ID, 'com.tencent.wework:id/er6').send_keys(number)

        self.find(MobileBy.XPATH,
                                 '//*[@resource-id="com.tencent.wework:id/av4" and @text="设置部门"]').click()
        self.find(MobileBy.ID, 'com.tencent.wework:id/fny').click()
        self.find(MobileBy.ID, 'com.tencent.wework:id/gvy').click()


        return InviteMember(self._driver)

