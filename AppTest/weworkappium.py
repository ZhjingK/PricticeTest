from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWework():
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "true"
        caps["skipServerInstallation"] = True
        caps["skipDeviceInitialization"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_add_member(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录" and @resource-id="com.tencent.wework:id/drk"]').click()

        # 如果成员很多，需要边滑动边查找"添加成员"元素是否存在
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()

        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()

        # 通过分级去定位，招到同级节点的父节点，根据父节点找子节点
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@resource-id="com.tencent.wework:id/au_"]').send_keys("静")
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/au_" and @text="必填"]').send_keys("静")

        # 更改性别为 女
        self.driver.find_element(MobileBy.XPATH, '//*[@text="性别"]/..//*[@resource-id="com.tencent.wework:id/av4"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()

        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/er6').send_keys('13678654323')
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/av4" and @text="设置部门"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fny').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gvy').click()

        print(self.driver.page_source)

