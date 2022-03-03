import time
import unittest

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import Base

timeformat = '%Y-%m-%dT%H:%M:%S'


class FacebookApp(Base):
    start_x = 860
    start_y = 1597
    end_x = 943
    end_y = 90
    duration = 300
    playing_time = 10

    def test_open_facebook_app(self):
        print("\n" + "________Facebook app")

        # scroll down to Facebook app
        self.driver.swipe(self.start_x, self.start_y, self.end_x, self.end_y, self.duration)

        # open Facebook app
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Facebook').click()
        print('Opened app at ' + self.driver.get_device_time())

        # verify the Facebook screen opened
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "facebook logo")))

        # tap Watch icon
        self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@bounds="[180,209][360,341]"]').click()

        # verify the Watch screen opened
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Watch")))

        # # get the name of the video
        # ls = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.view.ViewGroup')
        # for video in ls:
        #     if video.get_attribute("content-desc") is not None:
        #         print("video name is: ", video.get_attribute("accessibility id"))
        #         # break

        # Tap the first video
        self.driver.find_element(AppiumBy.XPATH,
                                 '//android.view.ViewGroup[@content-desc="Video"]/android.widget.FrameLayout/android.view.View').click()
        print('Video started at ' + self.driver.get_device_time())

        # verify the More Videos screen opened
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'More Videos')))

        # get the name of the video
        ls = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.view.ViewGroup')
        for video in reversed(ls):
            if video.get_attribute("content-desc") is not None:
                print("video name is: ", video.get_attribute("content-desc"))
                break

        # watch the video
        time.sleep(self.playing_time)
        print("Playing duration: ", self.playing_time)

        # Terminate the app and Tap Home button
        self.driver.terminate_app('com.facebook.katana')
        self.driver.press_keycode(3)
        print('Video ended at ' + self.driver.get_device_time())

    # def teardown(self):
    #     self.driver.quit()


if __name__ == "__main__":
    unittest.main()


