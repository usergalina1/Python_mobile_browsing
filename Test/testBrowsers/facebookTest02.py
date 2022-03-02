import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
timeformat = '%Y-%m-%dT%H:%M:%S'

class FacebookApp:
    def setup(self):
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                                       desired_capabilities={"deviceName": "988a5c474637494d4b ", "version": "9",
                                                             "platformName": "Android",
                                                             "automationName": "UIAutomator2",})

        self.driver.implicitly_wait(10)

    def test_open_facebook_app(self):
        print('Started at ' + time.strftime(timeformat))
        self.driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@content-desc="Facebook"]').click()
        time.sleep(3)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Watch, tab 3 of 6').click()
        # self.driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Watch"]').click()
        time.sleep(3)
        self.driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="Video"]').click()
        time.sleep(10)
        self.driver.press_keycode(3)
        print('Ended at ' + time.strftime(timeformat))

    def teardown(self):
        self.driver.quit()


if __name__=="__main__":
    f=FacebookApp()
    f.setup()
    f.test_open_facebook_app()
    f.teardown()
