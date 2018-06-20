"""
Module containing wrapper class for Selenium Web.
"""
from selenium.webdriver.remote.webelement import WebElement, By
from selenium.webdriver.common.action_chains import ActionChains
from .decorators import retry_with_timeout



class ExtendedWebElement:
    """
    Extends web elements with additional functionality.
    """

    def __init__(self, driver, name: str, locator: str, by: By = By.CSS_SELECTOR, nth_of_type=1):
        """
        Initializes ExtendedWebElement with Selenium WebElement.
        :param driver: CustomSeleniumDriver
        :param name: human-friendly name for element
        :param locator: property value
        :param by: (optional) property by which to find element (default CSS)
        :param nth_of_type: (optional) index of element in list of elements if more than one expected to match locator
        """
        self.driver = driver
        self.name = name
        self.locator = locator
        self.by = by
        self.nth_of_type = nth_of_type
        self.__element = None

    @property
    def element(self):
        if self.__element is None:
            self.__element = self.driver.driver.find_element(self.by, self.locator)

        return self.__element

    # Overwritten methods from WebElement
    @property
    def text(self):
        """The text (or value if input) of the element."""
        text = ''
        if self.element.tag_name == 'input':
            text = self.element.get_attribute('value')
        else:
            text =  self.element.text

        # If still no text, try 'innerText' attribute
        if text is None or len(text) == 0:
            text = self.element.get_attribute("innerText") or ''

        return text.strip()

    @property
    def text_raw(self):
        """The raw 'text' attribute of an element, regardless of tag_name"""
        return self.element.text

    @retry_with_timeout
    def set_value(self, text_value: str):
        """
        Set value in text field, clearing preexisting content.
        :param text_value: Text value to element
        """
        self.element.clear()
        self.element.send_keys(text_value)

    def click_js(self):
        """Click element using javascript (does not require element visibility)"""
        css_selector = self.convert_locator_to_css()
        self.driver.execute_script(f'document.querySelector("{css_selector}").click()')

    @retry_with_timeout
    def double_click(self):
        actions = ActionChains(self.driver)
        actions.double_click(self.element)
        actions.perform()

    # Simple pass-throughs from WebElement
    @retry_with_timeout
    def click(self):
        self.element.click()

    @property
    def tag_name(self):
        return self.element.tag_name

    def submit(self):
        self.element.submit()

    @retry_with_timeout
    def clear(self):
        self.element.clear()

    def get_property(self, name):
        return self.element.get_property(name)

    def get_attribute(self, name):
        return self.element.get_attribute(name)

    @property
    def is_selected(self):
        return self.element.is_selected

    @property
    def is_enabled(self):
        return self.element.is_enabled()

    @retry_with_timeout
    def send_keys(self, value):
        self.element.send_keys(value)

    @property
    def is_displayed(self):
        return self.element.is_displayed()

    @property
    def size(self):
        return self.element.size

    @property
    def location(self):
        return self.element.location

    @property
    def rect(self):
        return self.element.rect

    # Other methods
    def convert_locator_to_css(self):
        """Returns element locator as css selector string"""
        if self.by is By.CSS_SELECTOR:
            return self.locator
        elif self.by is By.ID:
            return f'#{self.locator}'
        elif self.by is By.CLASS_NAME:
            return f'.{self.locator}'
        elif self.by is By.TAG_NAME:
            return self.locator
        elif self.by in [By.NAME]:
            return f'[name="{self.locator}"]'
        else:
            raise NotImplementedError(f"Cannot convert {self.by} to css selector")
