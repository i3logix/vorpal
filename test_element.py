from vorpal import ExtendedWebElement, By
from unittest import mock
import pytest

@pytest.fixture
def default_element_data():
    return {
        'name':'name',
        'locator': 'locator',
        'by': By.CSS_SELECTOR
    }

@pytest.fixture
def element_and_drivers():
    driver_mock = mock.MagicMock(name='driver')
    element_mock = mock.MagicMock(name='element')
    driver_mock.driver.find_element.return_value = element_mock
    driver = driver_mock

    return (ExtendedWebElement(driver, 'name', 'locator', By.CSS_SELECTOR), driver_mock, element_mock)
    

def test_constructor(default_element_data):
    driver = None
    ExtendedWebElement(driver, *default_element_data)

def test_get_element(element_and_drivers):
    e, driver, _ = element_and_drivers
    e.text
    driver.driver.find_element.assert_called_once

def test_element_cached(element_and_drivers):
    e, driver, element_mock = element_and_drivers

    e.click()
    e.click()
    driver.driver.find_element.assert_called_once
    
    element_mock.click.assert_called()
    assert(len([call for call in element_mock.mock_calls if call == call.click()]) == 2)

def test_click_js(element_and_drivers):
    e, driver, element_mock = element_and_drivers

    e.click_js()

    driver.execute_script.assert_called_once_with('document.querySelector("locator").click()')

def test_set_value(element_and_drivers):
    e, driver, element_mock = element_and_drivers

    e.set_value('a')

    element_mock.clear.assert_called_once
    element_mock.send_keys.assert_called_once_with('a')

def test_text_raw(element_and_drivers):
    e, driver, element_mock = element_and_drivers

    element_mock.text = 'a'

    val = e.text_raw
    assert(val == 'a')

@pytest.mark.parametrize('tag_name,expected',[
    ('input', 'a'),
    ('h1', 'b'),
    ('input', ''),
])
def test_text(element_and_drivers, tag_name, expected):
    """
    Test the text property
    This property accesses the selenium element 'value' for inputs,
        'text' for non-inputs and 'innerText' if no text found in value/text attribute
    """
    e, driver, element_mock = element_and_drivers

    element_mock.tag_name = tag_name
    element_mock.get_attribute.return_value = expected
    element_mock.text = 'b'

    assert(e.text == expected)

def test_click(element_and_drivers):
    e, driver, element_mock = element_and_drivers

    e.click()
    element_mock.click.assert_called_once()

def test_submit(element_and_drivers):
    e, driver, element_mock = element_and_drivers

    e.submit()
    element_mock.submit.assert_called_once()

def test_clear(element_and_drivers):
    e, driver, element_mock = element_and_drivers

    e.clear()
    element_mock.clear.assert_called_once()

def test_get_property(element_and_drivers):
    e, driver, element_mock = element_and_drivers

    e.get_property('')
    element_mock.get_property.assert_called_once_with('')

def test_get_attribute(element_and_drivers):
    e, driver, element_mock = element_and_drivers

    e.get_attribute('')
    element_mock.get_attribute.assert_called_once_with('')

def test_send_keys(element_and_drivers):
    e, driver, element_mock = element_and_drivers

    e.send_keys('')
    element_mock.send_keys.assert_called_once_with('')

def test_tag_name(element_and_drivers):
    e, driver, element_mock = element_and_drivers
    element_mock.tag_name = 'a'

    assert(e.tag_name == 'a')

def test_is_selected(element_and_drivers):
    e, driver, element_mock = element_and_drivers
    element_mock.is_selected = 'a'

    assert(e.is_selected == 'a')

def test_is_enabled(element_and_drivers):
    e, driver, element_mock = element_and_drivers
    element_mock.is_enabled.return_value = 'a'

    assert(e.is_enabled == 'a')

def test_is_displayed(element_and_drivers):
    e, driver, element_mock = element_and_drivers
    element_mock.is_displayed.return_value = 'a'

    assert(e.is_displayed == 'a')

def test_size(element_and_drivers):
    e, driver, element_mock = element_and_drivers
    element_mock.size = 'a'

    assert(e.size == 'a')

def test_location(element_and_drivers):
    e, driver, element_mock = element_and_drivers
    element_mock.location = 'a'

    assert(e.location == 'a')

def test_rect(element_and_drivers):
    e, driver, element_mock = element_and_drivers
    element_mock.rect = 'a'

    assert(e.rect == 'a')

@pytest.mark.parametrize('by,expected', [
    (By.NAME, '[name="locator"]'),
    (By.ID, '#locator'),
    (By.CSS_SELECTOR, 'locator'),
    (By.CLASS_NAME, '.locator'),
    (By.TAG_NAME, 'locator'),
])
def test_convert_locator_to_css(by, expected):
    driver_mock = mock.MagicMock(name='driver')
    element_mock = mock.MagicMock(name='element')
    driver_mock.driver.find_element.return_value = element_mock
    driver = driver_mock
    e = ExtendedWebElement(driver, 'name', 'locator', by)

    assert(e.convert_locator_to_css() == expected)

@pytest.mark.parametrize('by', [
    By.XPATH,
    By.LINK_TEXT,
    By.PARTIAL_LINK_TEXT
])
def test_convert_locator_to_css_errorc(by):
    driver_mock = mock.MagicMock(name='driver')
    element_mock = mock.MagicMock(name='element')
    driver_mock.driver.find_element.return_value = element_mock
    driver = driver_mock
    e = ExtendedWebElement(driver, 'name', 'locator', by)
    try:
        e.convert_locator_to_css()
        raise Exception("Expected NotImplementedError")
    except NotImplementedError:
        pass

