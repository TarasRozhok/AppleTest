import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class MoveHelper:

    def __init__(self, app):
        self.app = app

    def move_to_element_helper(self, footer_item):
        driver = self.app.driver
        move = driver.find_element_by_css_selector("[data-analytics-title='%s']" % footer_item)
        ActionChains(driver).move_to_element(move).perform()