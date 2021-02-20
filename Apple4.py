from Application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_apple_ipad(app):
    app.open_home_page()
    app.click_on_search_field()
    app.send_kyes_mac()
    app.printed_mac_and_assert_mac_accessories()

