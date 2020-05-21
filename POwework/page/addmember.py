from time import sleep

from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMember():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self):
        # 为各个项sendkeys
        element = self.driver.find_element(By.ID, 'username')
        element.send_keys("kongtianlong")
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys("112")
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys("11111111112")

        # 下滑到底部
        touch = TouchActions(self.driver)
        touch.scroll_from_element(element, 0, 10000).perform()

        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

    def get_member(self):
        '''
        验证添加成员是否成功
        :return:
        '''
        elements = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # list = []
        # for element in elements:
        #     print(element)
        #     list.append(element.get_attribute("title"))
        # return list
        return [element.get_attribute("title") for element in elements]



