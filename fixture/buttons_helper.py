import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ButtonsHelper:

    def __init__(self, app):
        self.app = app

    def click_on_button_buy_in_airpods_menu(self, button_buy_on_page):
        driver = self.app.driver
        driver.find_element_by_css_selector("[aria-label='%s']" % button_buy_on_page).click()