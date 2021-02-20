def test_apple_airpods_max(app):
    app.open_home_page()
    app.all_menu.click_on_main_menu_item("iphone")
    app.all_menu.click_on_secondary_menu_item("airpods")
    assert 'Magic runs' in app.driver.find_element_by_css_selector(".section-hero").text
    app.buttons.click_on_button_buy_in_airpods_menu("Buy AirPods Max")
    assert 'Buy AirPods Max' in app.driver.find_element_by_css_selector("#page").text