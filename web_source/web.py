from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


class Web(object):
    __TIMEOUT = 10

    def __init__(self, web_driver):
        super(Web, self).__init__()
        self._web_driver_wait = WebDriverWait(web_driver, Web.__TIMEOUT)
        self._web_driver = web_driver

    def open(self, url):
        self._web_driver.get(url)

    def find_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def finds_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def find_by_id(self, element_id):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.ID, element_id)))

    def finds_by_id(self, element_id):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.ID, element_id)))

    def is_enabled_by_id(self, element_id):
        w_el = self.find_by_id(element_id)
        return w_el.is_enabled()

    def send_keys_by_id(self, element_id, _send_keys):
        self.finds_by_id(element_id)[0].click()
        self.finds_by_id(element_id)[0].clear()
        self.finds_by_id(element_id)[0].send_keys(_send_keys)

    def finds_by_tag_name(self, tag_name):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, tag_name)))

    def find_by_tag_name(self, tag_name):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.TAG_NAME, tag_name)))

    def finds_by_tag_name_for_element(self, parent_element, tag_name):
        return parent_element.find_elements(By.TAG_NAME, tag_name)

    def get_current_url(self):
        return self._web_driver.current_url

    def click_element_by_id(self, element_id):
        el = self.find_by_id(element_id)
        time.sleep(1)
        el.click()

    def click_element(self, web_element):
        time.sleep(1)
        web_element.click()

    def get_element_text_by_id(self, element_id):
        el = self.find_by_id(element_id)
        return el.text

    def get_browser_errors(self):
        for entry in self._web_driver.get_log('browser'):
            print("browser error level " + entry["level"])
            print("browser error message " + entry["message"])
        return self._web_driver.get_log('browser')
