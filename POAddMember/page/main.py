from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from POAddMember.page.BasePage import BasePage
from POAddMember.page.addmember import AddMember


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#"

    # def goto_add_member(self):
    #     # 点击添加成员
    #     # self.driver.find_element_by_xpath('//*[@class="index_top_operation_loginBtn"]').click()
    #     self._driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
    #     # 返回到添加成员页面
    #     return AddMember(self._driver)
    #
    # def goto_phone(self):
    #     self._driver.find_element(By.ID, "menu_contacts").click()
    #     sleep(2)
    #     self._driver.find_element(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
    #
    #     return AddMember(self._driver)

    def goto_add_member(self):
        # 点击添加成员
        # self.driver.find_element_by_xpath('//*[@class="index_top_operation_loginBtn"]').click()
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        # 返回到添加成员页面
        return AddMember(self._driver)

    def goto_phone(self):
        self.find(By.ID, "menu_contacts").click()
        sleep(2)
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()

        return AddMember(self._driver)