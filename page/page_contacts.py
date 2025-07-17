from appium.webdriver.common.appiumby import AppiumBy
from utils.utils_get_element import UtilsGetElement


class PageContacts(UtilsGetElement):
    # +号按钮
    add_button = 810, 1512
    dismiss_button = AppiumBy.ID, 'com.android.contacts:id/left_button'
    input2 = AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("名字")'
    all_number = AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.contacts:id/cliv_name_textview")'

    def add_click(self):
        self.touch_tag(x=810, y=1512)

    def dismiss_click(self):
        self.click(self.dismiss_button)

    def number_text(self):
        return self.more_text(self.all_number, 0)
