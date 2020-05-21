from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from POwework.page.addmember import AddMember


class Main():
    def __init__(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def goto_add_member(self):
        # 点击添加成员
        # self.driver.find_element_by_xpath('//*[@class="index_top_operation_loginBtn"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        # 返回到添加成员页面
        return AddMember(self.driver)