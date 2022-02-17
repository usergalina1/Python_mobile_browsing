import unittest

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestSelectRadioStation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                                       desired_capabilities=
                                       {
                                           "deviceName": "04RAYV406P ",
                                           "version": "12.0",
                                           "platformName": "Android",
                                           "automationName": "UIAutomator2",
                                       })

        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    start_x = 460
    start_y = 897
    end_x = 543
    end_y = 90
    duration = 300

    def test_open_iHeartRadio(self):
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
        print("\n" + station_title.get_attribute('text'))

        # tap the first playback in the list and play the first song
        self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.view.ViewGroup')[2].click()
        self.driver.find_element(AppiumBy.ID,
                                 'com.clearchannel.iheartradio.controller:id/catalog_item_content_slot').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Continue Listening"]').click()
        print("\n" + "Start time: ", self.driver.get_device_time())

        # retrive song, singer
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


if __name__ == '__main__':
    unittest.main()
