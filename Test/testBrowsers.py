import time
import unittest

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestBrowsers:

    def setup(self):
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

    websites = [
        'https://www.nbc.com/',
        'https://www.discovery.com/tv-shows/gold-rush/',
        'https://www.buzzfeed.com/',
        'http://www.espn.com/watch',
        'https://aiuto.libero.it/',
        'https://www.tgcom24.mediaset.it/',
        'http://www.raisport.rai.it/',
        'https://www.starbene.it/',
        'https://www.9now.com.au/',
        'https://www.gumtree.com.au/'
    ]
    start_x = 860
    start_y = 1597
    end_x = 943
    end_y = 90
    duration = 300
    time = 5

    def file_time_of_websites(self, website, browser):
        file = open("C:/Users/gademysh2001/Documents/Android Automation/GIT/webbrowsing.txt", 'a')
        file.write("\n " + browser + ": " + website + self.driver.get_device_time())
        file.close()

    def test_open_chrome_browser(self):
        self.browser = "Chrome"
        self.open_browser = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Chrome")
        self.open_browser.click()
        # open websites
        for i in self.websites:
            search_bar = self.driver.find_element(AppiumBy.ID, "com.android.chrome:id/search_box_text")
            self.driver.set_value(search_bar, i)
            self.driver.execute_script('mobile: performEditorAction',
                                       {
                                           'action': 'go'})
            print("Website:" + i, self.driver.get_device_time())
            self.file_time_of_websites(i, self.browser)
            time.sleep(self.time)

            tab_icon = self.driver.find_element(AppiumBy.ID, "com.android.chrome:id/tab_switcher_button")
            tab_icon.click()
            if i != self.websites[-1]:
                open_new_tab = self.driver.find_element_by_accessibility_id("New tab")
                open_new_tab.click()
            elif i == self.websites[-1]:
                continue
        # close all tabs
        self.driver.find_element(AppiumBy.ID, 'com.android.chrome:id/menu_button').click()
        self.driver.find_element_by_accessibility_id('Close all tabs').click()
        # press Home button
        self.driver.press_keycode(3)

    def test_open_opera_browser(self):
        self.browser = "Opera"
        self.driver.swipe(self.start_x, self.start_y, self.end_x, self.end_y, self.duration)
        self.driver.swipe(self.start_x, self.start_y, self.end_x, self.end_y, self.duration)
        self.open_browser = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Opera"]')
        self.open_browser.click()
        # open websites
        search_bar = self.driver.find_element(AppiumBy.ID, 'com.opera.browser:id/url_field')
        search_bar.clear()
        for i in self.websites:
            self.driver.set_value(search_bar, i)
            self.driver.execute_script('mobile: performEditorAction',
                                       {
                                           'action': 'go'})
            print("Website:" + i, self.driver.get_device_time())

            self.file_time_of_websites(i, self.browser)

            time.sleep(self.time)
            search_bar.click()
            search_bar.clear()
        # press Home button
        self.driver.press_keycode(3)

    def test_open_duckduckgo_browser(self):
        self.browser = "DuckDuckGo"
        self.driver.swipe(self.start_x, self.start_y, self.end_x, self.end_y, self.duration)
        self.open_browser = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DuckDuckGo")
        self.open_browser.click()
        # open websites
        for i in self.websites:
            search_bar = self.driver.find_element(AppiumBy.ID, "com.duckduckgo.mobile.android:id/omnibarTextInput")
            search_bar.send_keys(i)
            self.driver.press_keycode(66)

            print("Website:" + i, self.driver.get_device_time())
            self.file_time_of_websites(i, self.browser)

            time.sleep(self.time)
            if i != self.websites[-1]:
                tap_count_tab = self.driver.find_element(AppiumBy.ID, "com.duckduckgo.mobile.android:id/tabCount")
                tap_count_tab.click()
                open_new_tab = self.driver.find_element(AppiumBy.ID, "com.duckduckgo.mobile.android:id/newTab")
                open_new_tab.click()
            elif i == self.websites[-1]:
                continue
        # close all tabs
        self.driver.find_element(AppiumBy.ID, 'com.duckduckgo.mobile.android:id/tabCount').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Close All Tabs"]').click()
        # press Home button
        self.driver.press_keycode(3)


if __name__ == '__main__':
    unittest.main()
