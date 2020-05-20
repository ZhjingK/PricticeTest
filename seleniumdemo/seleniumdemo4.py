# selenium中执行js
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from seleniumdemo.base import Base


class TestJs(Base):
    @pytest.mark.skip
    def test_js(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")

        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()

        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element(By.XPATH, '//*[@class="n"]').click()

        for code in[
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    def test_time(self):
        '''
        取消时间控件的readonly属性，重新赋值
        :return:
        '''
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date')", "a.removeAttribute('readonly')")

        self.driver.execute_script("document.getElementById('train_date').value='2020-5-21'")
        sleep(3)


