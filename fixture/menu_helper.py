import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AdminCagesHelper:

    def __init__(self, app):
        self.app = app


    def click_on_menu_item(self, menu_item):
        driver = self.app.driver
        driver.find_element_by_css_selector(".ac-gn-link-%s" % menu_item).click()