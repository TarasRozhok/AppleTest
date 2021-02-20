def test_apple_tv(app):
    app.open_home_page()
    app.all_menu.click_on_main_menu_item("tv")
    app.all_menu.click_on_secondary_menu_item("tv-plus")
    app.click_button_watch_now()
    assert 'Start Your Free Trial' in app.driver.find_element_by_css_selector(".landing-page").text
