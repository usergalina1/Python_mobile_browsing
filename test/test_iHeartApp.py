import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import Base


class TestiHeartRadioApp(Base):
    start_x = 460
    start_y = 897
    end_x = 543
    end_y = 90
    duration = 300
    playing_time = 10

    def test_open_iHeartRadio(self):
        print("\n" + "________iHeartRadio app")

        # scroll to iHeartRadio app
        self.driver.swipe(self.start_x, self.start_y, self.end_x, self.end_y, self.duration)
        self.driver.swipe(self.start_x, self.start_y, self.end_x, self.end_y, self.duration)

        # open app
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'iHeartRadio').click()
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located((By.ID, "com.clearchannel.iheartradio.controller:id/logo_image")))

        # tap Radio icon on the bottom
        self.driver.find_element(AppiumBy.ID, 'com.clearchannel.iheartradio.controller:id/menu_radio').click()

        # tap See all
        self.driver.find_element(AppiumBy.ID, 'com.clearchannel.iheartradio.controller:id/header_button').click()

        # select STAR 101.3 channel
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="STAR 101.3"]').click()
        station_title = self.driver.find_element(AppiumBy.XPATH,
                                                 '//android.widget.TextView[@resource-id="com.clearchannel.iheartradio.controller:id/title"]')
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(
            (By.XPATH, '//android.widget.TextView[@resource-id="com.clearchannel.iheartradio.controller:id/title"]')))
        print("\n" + "Radio station: " + station_title.get_attribute('text'))

        # tap the first playback in the list and play the first song
        self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.view.ViewGroup')[3].click()
        self.driver.find_element(AppiumBy.ID,
                                 'com.clearchannel.iheartradio.controller:id/catalog_item_content_slot').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Continue Listening"]').click()
        print("\n" + "Start time: ", self.driver.get_device_time())

        # listen the music
        time.sleep(self.playing_time)
        print("Playing duration: ", self.playing_time)

        # retrieve song, singer
        song = self.driver \
            .find_element(AppiumBy.XPATH,
                          '//android.widget.TextView[@resource-id="com.clearchannel.iheartradio.controller:id/title_textView"]') \
            .get_attribute('text')
        singer = self.driver \
            .find_element(AppiumBy.XPATH,
                          '//android.widget.TextView[@resource-id="com.clearchannel.iheartradio.controller:id/subtitle_textView"]') \
            .get_attribute('text')

        print("The song is " + song)
        print("The singer is " + singer)

        # Terminate the app and Tap Home button
        self.driver.terminate_app('com.clearchannel.iheartradio.controller')
        print("\n" + "End time: ", self.driver.get_device_time())
        self.driver.press_keycode(3)



if __name__ == '__main__':
    unittest.main()
