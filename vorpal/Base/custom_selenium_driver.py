"""
Package: Base
CustomSeleniumDriver class implementation.
Methods for adding the new functionality to selenium methods.
"""
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from .element import ExtendedWebElement
import time
import os


class CustomSeleniumDriver:

    def __init__(self, driver, implicit_wait=5) -> None:
        self.driver = driver
        self.implicit_wait = implicit_wait

    def get_by_type(self, locator: str) -> By:
        """
        Elements by attribute type.
        :param locator: Attribute Type of specific element.
        :return: BY.VALUE attribute.
        """
        locator = locator.lower()
        locators = {'id': By.ID, 'xpath': By.XPATH, 'css_selector': By.CSS_SELECTOR, 'name': By.NAME,
                    'link_text': By.LINK_TEXT, 'class': By.CLASS_NAME}

        return locators[locator]

    def get_element(self, locator: dict) -> ExtendedWebElement:
        """
        Find specific element on current web page.
        :param locator: {'Element name': Name, 'locator_type': 'xpath', 'locator': 'path to element'} of attribute.
        :return: Selenium element.
        """

        element_name = locator['Element name']
        locator_type = locator['locator_type']
        locator_info = locator['locator']

        by_type = self.get_by_type(locator_type.lower())
        return ExtendedWebElement(self, element_name, locator_info, by_type)

    def get_elements(self, locator: dict) -> list([ExtendedWebElement]):
        """
        Find specific elements on current web page.
        :param locator: {Name, Value, Type} of attribute.
        :return: List of Selenium element.
        """
        by_type = self.get_by_type(locator['locator_type'].lower())
        return self.find_elements(by_type, locator['locator'])

    def take_screen_shot(self, log_message: str, directory: str = "../Screenshots/") -> None:
        """
        Takes screen shot of current page and saves to the Screenshot directory.
        :param log_message: Message provided for logging.
        :param directory: The directory name for screenshots.
        :return: N/A
        """

        file_name = log_message + "." + str(round(time.time() * 1000)) + ".png"

        current_directory = os.path.dirname(__file__)
        file_path = directory + file_name
        destination_file = os.path.join(current_directory, file_path)
        destination_directory = os.path.join(current_directory, directory)

        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        self.driver.save_screenshot(destination_file)

    def element_explicit_wait(self, locator: dict, timeout: int = 10, frequency: float = 0.5) -> ExtendedWebElement:
        """
        Explicitly wait for an element on current page to be interactive.
        :param locator: locator of an element.
        :param timeout: Maximum number of seconds for element to be interactive.
        :param frequency: Frequency at which webdriver checks to see if element is active.
        :return: WebElement object
        """

        by_type = self.get_by_type(locator['locator_type'])
        wait = WebDriverWait(
            self.driver,
            timeout=timeout,
            poll_frequency=frequency,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotSelectableException,
                ElementNotVisibleException])

        wait.until(ec.element_to_be_clickable((by_type, locator['locator'])))
        return ExtendedWebElement(self, locator['Element name'], locator['locator'], by_type)

    def scroll_window(self, direction: str) -> None:
        """
        Scroll current window up or down.
        :param direction: Direction of scroll.
        """
        direction = str(-1000) if direction == "up" else str(1000)
        self.driver.execute_script("window.scrollBy(0, " + direction + ");")

    # SECTION: Overwritten webdriver functions defined below
    def close(self):
        self.driver.close()

    @property
    def title(self):
        return self.driver.title

    @property
    def mobile(self):
        return self.driver.mobile

    @property
    def name(self):
        return self.driver.name

    def get(self, url):
        self.driver.get(url)

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def execute_async_script(self, script, *args):
        return self.driver.execute_async_script(script, *args)

    @property
    def current_url(self):
        return self.driver.current_url

    def quit(self):
        self.driver.quit()

    def maximize_window(self):
        self.driver.maximize_window()

    def fullscreen_window(self):
        self.driver.fullscreen_window()

    def minimize_window(self):
        self.driver.minimize_window()

    # SECTION: Individual web elements
    def find_element(self, by, value, element_name=None):
        return ExtendedWebElement(self, element_name, value, by)

    def find_element_by_class_name(self, name, element_name=None):
        return ExtendedWebElement(self, element_name, name, By.CLASS_NAME)

    def find_element_by_css_selector(self, css_selector, element_name=None):
        return ExtendedWebElement(self, element_name, css_selector, By.CSS_SELECTOR)

    def find_element_by_id(self, id, element_name=None):
        return ExtendedWebElement(self, element_name, id, By.ID)

    def find_element_by_link_text(self, link_text, element_name=None):
        return ExtendedWebElement(self, element_name, link_text, By.LINK_TEXT)

    def find_element_by_name(self, name, element_name=None):
        return ExtendedWebElement(self, element_name, name, By.NAME)

    def find_element_by_partial_link_text(self, partial_link_text, element_name=None):
        return ExtendedWebElement(self, element_name, partial_link_text, By.PARTIAL_LINK_TEXT)

    def find_element_by_tag_name(self, tag_name, element_name=None):
        return ExtendedWebElement(self, element_name, tag_name, By.TAG_NAME)

    def find_element_by_xpath(self, xpath, element_name=None):
        return ExtendedWebElement(self, element_name, xpath, By.XPATH)

    # SECTION: Web element collections

    def find_elements(self, by, value):
        element_count = len(self.driver.find_elements(by, value))
        return [ExtendedWebElement(self, None, value, by, index) for index in range(1, element_count + 1)]

    def find_elements_by_class_name(self, name):
        element_count = len(self.driver.find_elements_by_class_name(self, name))
        return [ExtendedWebElement(self, None, name, By.CLASS_NAME, index) for index in range(1, element_count + 1)]

    def find_elements_by_css_selector(self, css_selector):
        element_count = len(self.driver.find_elements_by_css_selector(self, css_selector))
        return [ExtendedWebElement(self, None, css_selector, By.CSS_SELECTOR, index) for index in range(1, element_count + 1)]

    def find_elements_by_id(self, id):
        element_count = len(self.driver.find_elements_by_id(self, id))
        return [ExtendedWebElement(self, None, id, By.ID, index) for index in range(1, element_count + 1)]

    def find_elements_by_link_text(self, link_text):
        element_count = len(self.driver.find_elements_by_link_text(self, link_text))
        return [ExtendedWebElement(self, None, link_text, By.LINK_TEXT, index) for index in range(1, element_count + 1)]

    def find_elements_by_name(self, name):
        element_count = len(self.driver.find_elements_by_name(self, name))
        return [ExtendedWebElement(self, None, name, By.NAME, index) for index in range(1, element_count + 1)]

    def find_elements_by_partial_link_text(self, partial_link_text):
        element_count = len(self.driver.find_elements_by_partial_link_text(self, partial_link_text))
        return [ExtendedWebElement(self, None, partial_link_text, By.PARTIAL_LINK_TEXT, index) for index in range(1, element_count + 1)]

    def find_elements_by_tag_name(self, tag_name):
        element_count = len(self.driver.find_elements_by_tag_name(self, tag_name))
        return [ExtendedWebElement(self, None, tag_name, By.TAG_NAME, index) for index in range(1, element_count + 1)]

    def find_elements_by_xpath(self, xpath):
        element_count = len(self.driver.find_elements_by_xpath(self, xpath))
        return [ExtendedWebElement(self, None, xpath, By.XPATH, index) for index in range(1, element_count + 1)]

    # SECTION: Navigation
    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    # SECTION: Options
    def get_cookies(self):
        return self.driver.get_cookies()

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def delete_cookie(self, name):
        self.driver.delete_cookiename(name)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def add_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    # SECTION: Timeouts
    def implicitly_wait(self, time_to_wait):
        self.driver.implicitly_wait(time_to_wait)

    def set_script_timeout(self, time_to_wait):
        self.driver.set_script_timeout(time_to_wait)

    def set_page_load_timeout(self, time_to_wait):
        self.driver.set_page_load_timeout(time_to_wait)

    # SECTION: Other
    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def get_window_size(self):
        return self.driver.get_window_size()

    @property
    def orientation(self):
        return self.driver.orientation

    @orientation.setter
    def orientation(self, value):
        """
        :param value: Either 'PORTRAIT' or 'LANDSCAPE'
        """
        self.driver.orientation = value


