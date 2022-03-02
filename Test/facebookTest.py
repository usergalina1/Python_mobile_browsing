import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

timeformat = '%Y-%m-%dT%H:%M:%S'


class FacebookApp:
    def setup(self):
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                                       desired_capabilities=
                                       {
                                           "deviceName": "04RAYV406P ",
                                           "version": "12.0",
                                           "platformName": "Android",
                                           "automationName": "UIAutomator2",
                                       })

        self.driver.implicitly_wait(10)

    start_x = 460
    start_y = 897
    end_x = 543
    end_y = 90
    duration = 300

    def test_open_facebook_app(self):
        # scroll down to Facebook app
        self.driver.swipe(self.start_x, self.start_y, self.end_x, self.end_y, self.duration)

        # open Facebook app
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Facebook').click()
        print('Opened app at ' + time.strftime(timeformat))

        # verify the Facebook screen opened
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "facebook logo")))

        # tap Watch icon
        self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@bounds="[360,209][540,341]"]').click()

        # verify the Watch screen opened
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Watch")))

        # Tap the first video
        self.driver.find_element(AppiumBy.XPATH,
                                 '//android.view.ViewGroup[@content-desc="Video"]/android.widget.FrameLayout/android.view.View').click()
        print('Video started at ' + time.strftime(timeformat))

        # verify the More Videos screen opened
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'More Videos')))

        # get the name of the video
        ls = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.view.ViewGroup')
        print(len(ls))
        for video in reversed(ls):
            if video.get_attribute("content-desc") is not None:
                print("video name is: ", video.get_attribute("content-desc"))
                break

        # watch the video
        time.sleep(50)
        # Terminate the app and Tap Home button
        self.driver.terminate_app('com.facebook.katana')
        self.driver.press_keycode(3)
        print('Video ended at ' + time.strftime(timeformat))

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    f = FacebookApp()
    f.setup()
    f.test_open_facebook_app()
    f.teardown()
