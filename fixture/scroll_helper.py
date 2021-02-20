import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ScrollHelper:

    def __init__(self, app):
        self.app = app

    def scroll_to_footer(self, scroll_to):
        driver = self.app.driver
        driver.find_element_by_css_selector("%s" % scroll_to).location_once_scrolled_into_view