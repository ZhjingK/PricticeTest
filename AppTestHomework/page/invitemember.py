from appium.webdriver.common.mobileby import MobileBy

from AppTestHomework.page.basepage import BasePage


class InviteMember(BasePage):
    def edit(self):
        # 互相导入会出现
        from AppTestHomework.page.editmember import EditMember
        # 点击手动输入添加
        # self._driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()

        return EditMember(self._driver)

    def get_toast(self):
        # return self._driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text

