def test_apple_airpods_max(app):
    app.open_home_page()
    app.admin_cages.click_on_menu_item(menu_item="iphone")
    app.click_om_secondary_menu_item(secondary_menu_item="airpods")
    app.assert_seconary_menu_item_name('AirPods Max')
    app.click_om_secondary_menu_item("airpods-max")
