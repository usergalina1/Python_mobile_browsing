import unittest

from appium import webdriver


class Base(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
