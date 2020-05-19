from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)

        self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, '//*[@name="f1"]/input[3]')
        element_dblick = self.driver.find_element(By.XPATH, '//*[@name="f1"]/input[2]')
        element_rightclick = self.driver.find_element(By.XPATH, '//*[@name="f1"]/input[4]')
        action = ActionChains(self.driver)
        # 点击
        action.click(element_click)
        # 右击
        action.context_click(element_rightclick)
        # 双击
        action.double_click(element_dblick)
        action.perform()
        sleep(5)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        element = self.driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        # 移动到某个元素
        action.move_to_element(element)
        sleep(2)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag = self.driver.find_element(By.XPATH, '//*[@id="dragger"]')
        drop1 = self.driver.find_element(By.XPATH, '//*[@class="item"][1]')
        drop2 = self.driver.find_element(By.XPATH, '//*[@class="item"][2]')
        drop3 = self.driver.find_element(By.XPATH, '//*[@class="item"][3]')
        action = ActionChains(self.driver)
        # 拖拽
        # action.drag_and_drop(drag, drop1)
        # sleep(2)
        # action.drag_and_drop(drag, drop2)
        # sleep(2)
        # action.drag_and_drop(drag, drop3)
        # sleep(2)
        action.click_and_hold(drag).release(drop1)
        sleep(2)
        action.click_and_hold(drag).release(drop2)
        sleep(2)
        action.click_and_hold(drag).release(drop3)
        sleep(2)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        element = self.driver.find_element_by_xpath("/html/body/label[1]/input")

        # 点击元素
        element.click()

        action = ActionChains(self.driver)
        # 输入并暂停
        action.send_keys("hello").pause(1)
        # 输入空格健
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        # 删除并暂停
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()
        sleep(2)

    def test_slide(self):
        self.driver.get("https://www.baidu.com/")
        element = self.driver.find_element_by_id("kw")
        element2 = self.driver.find_element_by_id("su")

        element.send_keys("selenium测试")
        touch = TouchActions(self.driver)
        touch.tap(element2)
        touch.perform()

        touch.scroll_from_element(element, 0, 10000).perform()

        self.driver.find_element_by_xpath('//*[@id="page"]/a[last()]')
        sleep(2)


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'seleniumdemo2'])