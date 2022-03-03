import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import Base


class TestYTMusicApp(Base):
    start_x = 860
    start_y = 1597
    end_x = 943
    end_y = 90
    duration = 300
    playing_time = 10

    def test_open_YTMusic(self):
        print("\n" + "________YouTube Music app")

        # scroll to YTMusic app
        self.driver.swipe(self.start_x, self.start_y, self.end_x, self.end_y, self.duration)
        self.driver.swipe(self.start_x, self.start_y, self.end_x, self.end_y, self.duration)
        self.driver.swipe(self.start_x, self.start_y, self.end_x, self.end_y, self.duration)

        # open app
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'YT Music').click()
        print('Opened app (FOREGROUND) at ' + self.driver.get_device_time())

        # verify the YT Music screen opened
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located((By.ID, "com.google.android.apps.youtube.music:id/toolbar")))

        # tap Relax button
        self.driver.find_elements(AppiumBy.ID, 'com.google.android.apps.youtube.music:id/chip_cloud_chip_text')[
            2].click()

        # tap first disc-container From the community
        self.driver.find_element(AppiumBy.ID,
                                 'com.google.android.apps.youtube.music:id/thumbnail_outer_container').click()

        # get the name of the composition
        ls = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')
        for song in ls:
            if song.get_attribute("text") is not None:
                print("\n" + "Music name  for METADATA is: ", song.get_attribute("text"))
                print("\n" + "TOTAL duration: ", song.get_attribute("text")[-4:])
                break

        # tap first composition in the list
        self.driver.find_element(AppiumBy.ID,
                                 'com.google.android.apps.youtube.music:id/two_column_item_content_parent').click()
        print("\n" + "Start time: ", self.driver.get_device_time())

        # listen the music
        time.sleep(self.playing_time)
        print("Playing (SIMPLE) duration: ", self.playing_time)

        # Terminate the app and Tap Home button
        self.driver.terminate_app('com.google.android.apps.youtube.music')
        print("\n" + "End time: ", self.driver.get_device_time())
        self.driver.press_keycode(3)


if __name__ == '__main__':
    unittest.main()
