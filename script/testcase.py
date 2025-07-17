import time

import allure
import pytest

from base.base_driver import BaseDriver
from page.page_addnum import PageAddNum
from page.page_contacts import PageContacts
from page.page_public import PagePublic
from utils.utils_get_data import utils_get_yaml_data, utils_get_json_data


class Testcase:
    def setup_class(self):
        self.driver = BaseDriver().get_driver('com.android.contacts', '.activities.PeopleActivity')
        self.driver.implicitly_wait(10)
        self.contact = PageContacts(self.driver)
        self.add_num = PageAddNum(self.driver)
        self.public = PagePublic(self.driver)

    def teardown_class(self):
        self.driver.get_screenshot_as_file('./screenshot/test1.png')
        self.driver.quit()

    # @pytest.mark.parametrize("test_data", utils_get_yaml_data('data.yaml','testcase'))
    @pytest.mark.parametrize("test_data", utils_get_json_data('data.json'))
    def test1(self, test_data):
        # allure.dynamic.title(r"Test with param: {test_data}")
        self.contact.add_click()
        # try:
        #     self.contact.dismiss_click()
        # except:
        #     pass
        self.add_num.input1_send(test_data['name'])
        self.add_num.input2_send(test_data['username'])
        self.add_num.input3_send(test_data['number'])
        self.add_num.input4_send(test_data['email'])
        self.add_num.save_click()
        print(self.add_num.get_save_message())
        self.public.key_back()
        result = self.contact.number_text()
        assert test_data['expect'] in result
