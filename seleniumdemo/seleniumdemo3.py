# 多窗口处理和网页frame
from time import sleep

import pytest
from selenium.webdriver.common.by import By

# from seleniumdemo.base import Base
from seleniumdemo.Bbase import BBase


class TestSwitchWindows(BBase):

    @pytest.mark.skip
    def test_switch_window(self):
        '''
        百度首页点击登录--立即注册--切换窗口句柄
        :return:
        '''
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="u1"]/a[2]').click()
        sleep(2)
        print(self.driver.current_window_handle)

        self.driver.find_element_by_link_text("立即注册").click()
        sleep(2)
        print(self.driver.current_window_handle)

        print(self.driver.window_handles)
        window = self.driver.window_handles
        self.driver.switch_to_window(window[-1])
        self.driver.find_element_by_xpath('//*[@name="userName"]').send_keys("hello")
        sleep(1)

        self.driver.switch_to_window(window[0])
        sleep(3)

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element(By.XPATH, '//*[@id="draggable"]').text)
        print(self.driver.find_element(By.XPATH, '//*[@id="droppable"]').text)

        self.driver.switch_to.parent_frame()
        self.driver.find_element(By.ID, 'submitBTN').click()


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'seleniumdemo3'])