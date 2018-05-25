"""
Package: Base
CustomSeleniumDriver class implementation.
Methods for adding the new functionality to selenium methods.
"""
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
import time
import os


class CustomSeleniumDriver:

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_title(self) -> str:
        """
        Return the current title of web page.
        :return: (string) Title of Page.
        """
        return self.driver.title

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

    def get_element(self, locator: dict) -> WebElement:
        """
        Find specific element on current web page.
        :param locator: {'Element name': Name, 'locator_type': 'xpath', 'locator_info': 'path to element'} of attribute.
        :return: Selenium element.
        """

        element_name = locator['Element name']
        locator_type = locator['locator_type']
        locator_info = locator['locator']

        by_type = self.get_by_type(locator_type.lower())
        element = self.driver.find_element(by_type, locator_info)
        return element

    def get_elements(self, locator: dict) -> list([WebElement]):
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
        return elements

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

    def element_explicit_wait(self, locator: dict, timeout: int = 10, frequency: float = 0.5) -> WebElement:
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
        return element

    def scroll_window(self, direction: str) -> None:
        """
        Scroll current window up or down.
        :param direction: Direction of scroll.
        """
        direction = str(-1000) if direction == "up" else str(1000)
        self.driver.execute_script("window.scrollBy(0, " + direction + ");")