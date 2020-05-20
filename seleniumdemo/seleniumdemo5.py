from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from seleniumdemo.base import Base


class TestInput(Base):
    @pytest.mark.skip
    def test_file_input(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@class="st_camera_off"]').click()
        self.driver.find_element_by_xpath('//*[@id="stfile"]').send_keys("/Users/zhangjing1/Desktop/practice/img/哒哒哒.png")
        sleep(3)

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换到按钮的frame下
        self.driver.switch_to_frame("iframeResult")
        drag = self.driver.find_element(By.XPATH, '//*[@id="draggable"]')
        drop = self.driver.find_element(By.XPATH, '//*[@id="droppable"]')

        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

        self.driver.switch_to_alert().accept()

        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(3)



