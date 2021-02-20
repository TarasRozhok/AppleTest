import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MenuHelper:

    def __init__(self, app):
        self.app = app


    def click_on_main_menu_item(self, menu_item):
        driver = self.app.driver
        driver.find_element_by_css_selector(".ac-gn-link-%s" % menu_item).click()

    def click_on_secondary_menu_item(self, secondary_menu_item):
        driver = self.app.driver
        driver.find_element_by_css_selector(".chapternav-item-%s" % secondary_menu_item).click()

    def click_on_foter_menu_item(self, footer_menu_item):
        driver = self.app.driver
        driver.find_element_by_css_selector("[data-analytics-title='%s']" % footer_menu_item).click()

    def click_on_alternative_footer_menu_item(self, alternative_footer_menu_item):
        driver = self.app.driver
        driver.find_element_by_css_selector('[data-display-name="%s"]' % alternative_footer_menu_item).click()
