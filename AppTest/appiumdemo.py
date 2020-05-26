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
    # 类的级别只初始化一次，不需要多次打开APP
    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = "true"
        caps["skipServerInstallation"] = True
        caps["skipDeviceInitialization"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def setup(self):
        pass

    def teardown_class(self):
        self.driver.quit()

    def teardown(self):
        # 增加返回的操作，便于下一个用例运行
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()

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

        # 断言逻辑：去找对应行是否有"已添加"的元素，有的话直接输出"已添加自选"，没有的话点击"加自选"

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
