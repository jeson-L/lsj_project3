from appium.webdriver.common.appiumby import AppiumBy

from utils.utils_get_element import UtilsGetElement


class PageAddNum(UtilsGetElement):
    input1 = AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("姓氏")'
    input2 = AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("名字")'
    input3 = AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("电话")'
    input4 = AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("电子邮件")'
    save_button = AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("保存")'
    save_message = AppiumBy.XPATH, '//*[contains(@text,"已保存")]'
    def save_click(self):
        self.click(self.save_button)

    def input1_send(self, value):
        self.send(self.input1, value)

    def input2_send(self, value):
        self.send(self.input2, value)

    def input3_send(self, value):
        self.send(self.input3, value)

    def input4_send(self, value):
        self.send(self.input4, value)

    def get_save_message(self):
        return self.one_text(self.save_message)
