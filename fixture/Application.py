import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from fixture.menu_helper import AdminCagesHelper

class Application:

    def __init__(self):
        # for headless mode
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())  # (options=options)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.all_menu = AdminCagesHelper(self)

    def scroll_to_accessories_for_apple_tv_and_click_shop(self):
        driver = self.driver
        driver.find_element_by_css_selector(
            "[aria-label='Shop now for Apple TV accessories']").location_once_scrolled_into_view
        driver.find_element_by_css_selector("[aria-label='Shop now for Apple TV accessories']").click()
        assert 'Siri Remote' in driver.find_element_by_css_selector("[data-display-name='Siri Remote 2017']").text


    def open_home_page(self):
        driver = self.driver
        driver.get("https://www.apple.com/")

    def click_om_secondary_menu_item(self, secondary_menu_item):
        driver = self.driver
        driver.find_element_by_css_selector(".chapternav-item-%s" % secondary_menu_item).click()

    def assert_seconary_menu_item_name(self, secondary_menu_item_name):
        driver = self.driver
        assert ('%s' % secondary_menu_item_name) in driver.find_element_by_css_selector(".chapternav-items").text

    def assert_535_dollars(self):
        driver = self.driver
        assert '$535' in driver.find_element_by_css_selector("[data-tradein-product='ipadpro-tradein']").text

    def printed_mac_and_assert_mac_accessories(self):
        driver = self.driver
        mac_accessories = driver.find_element_by_css_selector("[data-label='Mac Accessories']")
        ActionChains(driver).move_to_element(mac_accessories).perform()
        driver.find_element_by_css_selector("[data-label='Mac Accessories']").click()
        assert 'Featured Mac Accessories' in driver.find_element_by_css_selector(".accessories").text

    def send_kyes_mac(self):
        driver = self.driver
        driver.find_element_by_css_selector(".ac-gn-searchform-input").send_keys("Mac")

    def click_on_search_field(self):
        driver = self.driver
        driver.find_element_by_css_selector("#ac-gn-link-search").click()

    def click_button_watch_now(self):
        driver = self.driver
        driver.find_element_by_css_selector(".watch-element").click()

    def assert_free_trial_tv(self):
        driver = self.driver
        assert 'Start Your Free Trial' in driver.find_element_by_css_selector(".landing__header__content").text



    def destroy(self):
            self.driver.quit()
