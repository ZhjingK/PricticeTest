from appium import webdriver

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver is None:
            caps = {"platformName": "Android", "deviceName": "emulator-5554", "appPackage": "com.xueqiu.android",
                    "appActivity": ".view.WelcomeActivityAlias", "noReset": "true", "skipServerInstallation": True,
                    "skipDeviceInitialization": True}
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(3)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)

