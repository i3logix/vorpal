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

    def __init__(self, driver) -> None:
        self.driver = driver

    def __getattr__(self, attr):
        """
        Give direct access to the underlying selenium driver's methods
        """
        return getattr(self.driver, attr)

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
        element = self.driver.find_element(by_type, locator_info)
        return ExtendedWebElement(element, self)

    def get_elements(self, locator: dict) -> list([ExtendedWebElement]):
        """
        Find specific elements on current web page.
        :param locator: {Name, Value, Type} of attribute.
        :return: List of Selenium element.
        """

        element_name = locator['Element name']
        locator_type = locator['locator_type']
        locator_info = locator['locator']

        by_type = self.get_by_type(locator_type.lower())
        elements = self.driver.find_elements(by_type, locator_info)
        return [ExtendedWebElement(element, self) for element in elements]

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
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency,
                                ignored_exceptions=[NoSuchElementException, ElementNotSelectableException,
                                                    ElementNotVisibleException])
        element = wait.until(ec.element_to_be_clickable((by_type, locator['locator'])))
        return ExtendedWebElement(element, self)

    def scroll_window(self, direction: str) -> None:
        """
        Scroll current window up or down.
        :param direction: Direction of scroll.
        """
        direction = str(-1000) if direction == "up" else str(1000)
        self.driver.execute_script("window.scrollBy(0, " + direction + ");")

    # Overwritten webdriver functions defined below

    # SECTION: Individual web elements
    def find_element(self, by, value):
        return ExtendedWebElement(self.driver.find_element(by, value), self)

    def find_element_by_class_name(self, name):
        return ExtendedWebElement(self.driver.find_element_by_class_name(name), self)

    def find_element_by_css_selector(self, css_selector):
        return ExtendedWebElement(self.driver.find_element_by_css_selector(css_selector), self)

    def find_element_by_id(self, id):
        return ExtendedWebElement(self.driver.find_element_by_id(id), self)

    def find_element_by_link_text(self, link_text):
        return ExtendedWebElement(self.driver.find_element_by_link_text(link_text), self)

    def find_element_by_name(self, name):
        return ExtendedWebElement(self.driver.find_element_by_name(name), self)

    def find_element_by_partial_link_text(self, partial_link_text):
        return ExtendedWebElement(self.driver.find_element_by_partial_link_text(partial_link_text), self)

    def find_element_by_tag_name(self, tag_name):
        return ExtendedWebElement(self.driver.find_element_by_tag_name(tag_name), self)

    def find_element_by_xpath(self, xpath):
        return ExtendedWebElement(self.driver.find_element_by_xpath(xpath), self)

    # SECTION: Web element collections

    def find_elements(self, by, value):
        return [ExtendedWebElement(element, self) for element in self.driver.find_elements(by, value)]

    def find_elements_by_class_name(self, name):
        return [ExtendedWebElement(element, self) for element in self.driver.find_elements_by_class_name(name)]

    def find_elements_by_css_selector(self, css_selector):
        return [ExtendedWebElement(element, self) for element in self.driver.find_elements_by_css_selector(css_selector)]

    def find_elements_by_id(self, id):
        return [ExtendedWebElement(element, self) for element in self.driver.find_elements_by_id(id)]

    def find_elements_by_link_text(self, link_text):
        return [ExtendedWebElement(element, self) for element in self.driver.find_elements_by_link_text(link_text)]

    def find_elements_by_name(self, name):
        return [ExtendedWebElement(element, self) for element in self.driver.find_elements_by_name(name)]

    def find_elements_by_partial_link_text(self, partial_link_text):
        return [ExtendedWebElement(element, self) for element in self.driver.find_elements_by_partial_link_text(partial_link_text)]

    def find_elements_by_tag_name(self, tag_name):
        return [ExtendedWebElement(element, self) for element in self.driver.find_elements_by_tag_name(tag_name)]

    def find_elements_by_xpath(self, xpath):
        return [ExtendedWebElement(element, self) for element in self.driver.find_elements_by_xpath(xpath)]
