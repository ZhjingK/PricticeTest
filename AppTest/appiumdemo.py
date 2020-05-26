import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

'''
改造1：pytest格式
改造2：可维护的代码形态，不允许有绝对路径的存在
改造3：将自动生成的find_element_by_** 改造成find_element(MobileBy.**, "**")的形式
改造4：添加断言
'''


class TestXueQiu():
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('search,type,str', [
        ('alibaba', 'BABA', '已添加'),
        ('xiaomi', '01810', '已添加')
    ])
    def test_search(self, search, type, str):
        el1 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text")
        el2.click()
        el2.send_keys(search)
        el3 = self.driver.find_element(MobileBy.XPATH, f'//*[@text={type}]')
        el3.click()
        el3 = self.driver.find_element(MobileBy.XPATH, f'//*[@text={type}]/../../..//*[@resource-id="com.xueqiu.android:id/follow_btn"]')
        el3.click()
        element = self.driver.find_element(MobileBy.XPATH, f'//*[@text={type}]/../../..//*[@resource-id="com.xueqiu.android:id/followed_btn"]')

        assert str in element.get_attribute('text')

    # def test_search(self):
    #     el1 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")
    #     el1.click()
    #     el2 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text")
    #     el2.click()
    #     el2.send_keys("alibaba")
    #     el3 = self.driver.find_element(MobileBy.XPATH, '//*[@text="BABA"]')
    #     el3.click()
    #     el3 = self.driver.find_element(MobileBy.XPATH, '//*[@text="BABA"]/../../..//*[@resource-id="com.xueqiu.android:id/follow_btn"]')
    #     el3.click()
    #     element = self.driver.find_element(MobileBy.XPATH, '//*[@text="BABA"]/../../..//*[@resource-id="com.xueqiu.android:id/followed_btn"]')
    #
    #     assert "已添加" in element.get_attribute('text')