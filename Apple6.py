def test_all_menus(app):
    app.open_home_page()
    app.all_menu.click_on_main_menu_item("watch")
    app.all_menu.click_on_secondary_menu_item("bands")
    app.all_menu.click_on_alternative_footer_menu_item("Apple and Education")
    assert 'How to Buy' in app.driver.find_element_by_css_selector(".section-how-to-buy").text