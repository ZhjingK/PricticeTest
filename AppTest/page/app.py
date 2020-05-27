from appium import webdriver

from AppTest.page.basepage import BasePage
from AppTest.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver is None:
            caps = {"platformName": "Android", "deviceName": "emulator-5554", "appPackage": "com.tencent.wework",
                    "appActivity": ".launch.WwMainActivity", "noReset": "true", "skipServerInstallation": True,
                    "skipDeviceInitialization": True}
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # launch_app()方法是appium提供的直接启动应用
            # start_activity(appPackage="", appActivity="")方法需要提供package和activity才能启动应用
            self._driver.launch_app()

        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
