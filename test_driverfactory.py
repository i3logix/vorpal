from unittest import mock
import pytest
from vorpal import WebDriverFactory

@pytest.mark.parametrize("browser,expected",[
    ("firefox", 'Firefox'),
    ("IE", 'Ie'),
    ("chrome", 'Chrome'),
])
def test_get_webdriver_instance(browser, expected):    
    fake_webdriver = mock.MagicMock()
    wdf = WebDriverFactory(browser, '', fake_webdriver)
    wdf.get_webdriver_instance()
    getattr(fake_webdriver, expected).assert_called_once()
