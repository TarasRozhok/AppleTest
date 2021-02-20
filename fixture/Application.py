import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from fixture.menu_helper import MenuHelper
from fixture.buttons_helper import ButtonsHelper
from fixture.move_helper import MoveHelper
from fixture.scroll_helper import ScrollHelper

class Application:

    def __init__(self):
        # for headless mode
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())  # (options=options)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.all_menu = MenuHelper(self)
        self.buttons = ButtonsHelper(self)
        self.move = MoveHelper(self)
        self.scroll = ScrollHelper(self)


    def open_home_page(self):
        driver = self.driver
        driver.get("https://www.apple.com/")

    def assert_seconary_menu_item_name(self, secondary_menu_item_name):
        driver = self.driver
        assert ('%s' % secondary_menu_item_name) in driver.find_element_by_css_selector(".chapternav-items").text

    def printed_mac_and_assert_mac_accessories(self):
        driver = self.driver
        mac_accessories = driver.find_element_by_css_selector("[data-label='Mac Accessories']")
        ActionChains(driver).move_to_element(mac_accessories).perform()
        driver.find_element_by_css_selector("[data-label='Mac Accessories']").click()

    def send_kyes_mac(self):
        driver = self.driver
        driver.find_element_by_css_selector(".ac-gn-searchform-input").send_keys("Mac")

    def click_on_search_field(self):
        driver = self.driver
        driver.find_element_by_css_selector("#ac-gn-link-search").click()

    def click_button_watch_now(self):
        driver = self.driver
        driver.find_element_by_css_selector(".watch-element").click()





    def destroy(self):
            self.driver.quit()
