from appium.webdriver.common.mobileby import MobileBy

from AppTestHomework.page.basepage import BasePage


class ManageContacts(BasePage):
    def deletemember(self):
        try:
            element = self.find(MobileBy.XPATH, '//*[@text="静静"]')
        except:
            # 滑动查找需要删除的成员并点击
            element = self._driver.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("静静").instance(0))')

        element.click()

        # 滑动查找删除成员并点击
        self._driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("删除成员").instance(0))').click()

        # 点击弹窗上的确认
        self.find(MobileBy.XPATH, '//*[@text="确认"]').click()




