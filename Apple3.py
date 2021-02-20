from Application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_apple_ipad(app):
    app.open_home_page()
    app.click_on_menu_item(menu_item="ipad")
    app.click_om_secondary_menu_item(secondary_menu_item="ipad-pro")
    app.assert_535_dollars()