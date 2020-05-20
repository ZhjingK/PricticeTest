from selenium import webdriver
import os

# selenium多浏览器处理
# 使用这个命令在命令行运行：browser=chrome pytest seleniumdemo/seleniumdemo3.py


class BBase():
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.PhantomJS()

        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def teardown(self):
        self.driver.quit()
