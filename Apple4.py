def test_search_accessories(app):
    app.open_home_page()
    app.click_on_search_field()
    app.send_kyes_mac()
    app.printed_mac_and_assert_mac_accessories()
    assert 'Featured Mac Accessories' in app.driver.find_element_by_css_selector("#page").text

