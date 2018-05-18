"""
Module containing wrapper class for Selenium Web.
"""

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

class ExtendedWebElement:
    """
    Extends web elements with additional functionality.
    """

    def __init__(self, element: WebElement, driver):
        """
        Initializes ExtendedWebElement with Selenium WebElement.
        :param element: base Selenium WebElement
        :param driver: Selenium driver for methods that require knowledge of driver/browser
        """
        self.element = element
        self.driver = driver

    def __getattr__(self, attr):
        return getattr(self.element, attr)

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
        if len(text) == 0:
            text = self.element.get_attribute("innerText")
        
        return text.strip()
    
    @property
    def text_raw(self):
        """The raw 'text' attribute of an element, regardless of tag_name"""
        return self.element.text

    def set_value(self, text_value: str):
        """
        Set value in text field, clearing preexisting content.
        :param text_value: Text value to element
        """
        self.element.clear()
        self.element.send_keys(text_value)
    
    def double_click(self):
        actions = ActionChains(self.driver)
        actions.double_click(self.element)
        actions.perform()
