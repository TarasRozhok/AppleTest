from Application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_apple_tv(app):
    app.open_home_page()
    app.click_on_menu_item(menu_item="tv")
    app.click_om_secondary_menu_item(secondary_menu_item="tv-plus")
    app.click_button_watch_now()
    app.assert_free_trial_tv()
