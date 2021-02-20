def test_apple_ipad(app):
    app.open_home_page()
    app.all_menu.click_on_main_menu_item("ipad")
    app.all_menu.click_on_secondary_menu_item("ipad-pro")
    assert '$535' in app.driver.find_element_by_css_selector(".page-overview").text