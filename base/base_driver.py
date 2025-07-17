from appium import webdriver


class BaseDriver:
    def __init__(self):
        self.driver = None

    def get_driver(self, package, activity):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = 9
        desired_caps['deviceName'] = '*'
        desired_caps['appPackage'] = package
        desired_caps['appActivity'] = activity
        desired_caps['automationName'] = "UiAutomator2"
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return self.driver


