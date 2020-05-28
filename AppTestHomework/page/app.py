from appium import webdriver

from AppTestHomework.page.basepage import BasePage
from AppTestHomework.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver is None:
            caps = {"platformName": "Android", "deviceName": "emulator-5554", "appPackage": "com.tencent.wework",
                    "appActivity": ".launch.WwMainActivity", "noReset": "true", "skipServerInstallation": True,
                    "skipDeviceInitialization": True}
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(5)
        return self

    def main(self) -> Main:
        return Main(self._driver)
