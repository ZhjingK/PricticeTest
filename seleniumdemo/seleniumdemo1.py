from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo1():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://testerhome.com/")
        sleep(2)
        self.driver.find_element_by_link_text("社团").click()
        sleep(2)
        self.driver.find_element_by_link_text("霍格沃兹测试学院").click()

        # # 自定义until中需要的方法
        # def wait(x):
        #     return len(self.driver.find_elements(By.CSS_SELECTOR, ".topic-22359 .title > a")) >= 1
        # WebDriverWait(self.driver, 10).until(wait)

        # 使用selenium内置的条件expected_conditions
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#main > div > div.col-md-8 > div > div.panel-body > div.topic.media.topic-22359 > div.infos.media-body > div.title.media-heading > a')))

        self.driver.find_element_by_css_selector(".topic-22359 .title > a").click()
        sleep(2)


