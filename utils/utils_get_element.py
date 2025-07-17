import logging
from appium.webdriver.common.touch_action import TouchAction


class UtilsGetElement:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element):
        logging.info('正在通过（{}）方法，找单个：（{}）元素'.format(*element))
        return self.driver.find_element(*element)

    def find_elements(self, element):
        logging.info('正在通过（{}）方法，找多个：（{}）元素'.format(*element))
        return self.driver.find_elements(*element)

    def click(self, element):
        logging.info('正在对该：（{}）元素进行单击'.format(element))
        self.find_element(element).click()

    def clicks(self, element, n):
        logging.info('正在一组：（{}）元素的第 ：{} 个进行单击'.format(element, n))
        self.find_elements(element)[n].click()

    def send(self, element, value):
        logging.info('正在对该：（{}）元素进行进行输入：{}'.format(element, value))
        self.find_element(element).send_keys(value)

    def sends(self, element, value, n):
        logging.info('正在一组：（{}）元素的第：{} 个进行输入：{} '.format(element, n, value))
        self.find_element(element)[n].send_keys(value)

    def one_text(self, element):
        logging.info('正在获取：（{}）元素的文本'.format(element))
        text = self.find_element(element).text
        logging.info('获取到：（{}）元素的文本为：{}'.format(element, text))
        return text

    def more_text(self, element, n):
        logging.info('正在获取：（{}）元素的第：{}个文本'.format(element, n))
        text = self.find_elements(element)[n].text
        logging.info('获取到：（{}）元素的第：{}个文本为：{}'.format(element, n, text))
        return text

    def touch_tag(self, element=None, x=None, y=None):
        if x is not None or y is not None:
            logging.info('判断x为：{},y为：{},执行坐标轻敲'.format(x, y))
            TouchAction(self.driver).tap(x=x, y=y).perform()
        else:
            logging.info('判断x为：{},y为：{},执行元素{}轻敲'.format(x, y, element))
            TouchAction(self.driver).tap(element).perform()

    def keycode(self, keycode):
        logging.info('执行手机按键操作：{}'.format(keycode))
        self.driver.press_keycode(keycode)
