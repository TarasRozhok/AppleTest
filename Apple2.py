def test_apple_tv_with_move_and_scrolls(app):
    app.open_home_page()
    app.all_menu.click_on_main_menu_item("tv")
    app.all_menu.click_on_secondary_menu_item("airplay")
    assert 'AirPlay' in app.driver.find_element_by_css_selector(".page-overview").text
    app.scroll.scroll_to_footer(".ac-gf-breadcrumbs-home-icon").location_once_scrolled_into_view
    app.move.move_to_element_helper("mac")
    app.move.move_to_element_helper("ipad")
    app.move.move_to_element_helper("iphone")