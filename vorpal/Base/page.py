"""
Module containing base class for HTTP endpoints.
"""
from abc import ABC, abstractmethod

class BasePage(ABC):
    # Url for the page
    # Optional, but required for .goto() method
    url = None

    def __init__(self, driver, page_name):
        """
        Initializes the BaseHttpEndpoint class.
        :param driver: a CustomSeleniumDriver
        """
        self.driver = driver
        self.name = page_name

    def goto(self, **kwargs):
        """
        Uses driver to navigate to self.url if set, otherwise raises Exception
        :param **kwargs: keyword arguments converted into key=value query parameters
        """
        if self.url == None:
            raise Exception(f"Attempted to goto {self.name}, but no url was provided in class definition.")

        param_string = ''
        # Build query params if any provided
        if len(kwargs) > 0:
            param_string = '?'
            for key, value in kwargs.items():
                param_string += f"{key}={value}&"
        
        self.driver.driver.get(self.url + param_string)
        # Return self to allow chaining
        # e.g. login_page.goto().login()
        return self

    @abstractmethod
    def isCurrentPage(self):
        """
        (Abstract) Verifies that driver is on current page.
        """
        pass
