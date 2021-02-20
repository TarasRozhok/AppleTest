from Application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_apple_siri_remote(app):
    app.open_home_page()
    app.click_on_menu_item(menu_item="tv")
    app.scroll_to_accessories_for_apple_tv_and_click_shop()