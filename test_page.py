"Tests for page object implementation"
import pytest
from unittest.mock import Mock
from vorpal import webdriver, custom_selenium_driver, BasePage

class NoAbstractImplementation(BasePage):
    "Page object that doesn't implement abstract methods from BasePage"
    pass

def test_page_isabstract():
    "Assert instantiating a page without implementing abstract methods raises TypeError"
    with pytest.raises(TypeError):
        NoAbstractImplementation(None, "Bad Page")


class NoUrl(BasePage):
    "Page object with no url"
    def isCurrentPage(self):
        "Implements abstract method"
        return True

def test_goto_needs_url():
    "Assert page.goto() raises Exception if no url property provided in class definition"
    page = NoUrl(None, "No Url Page")
    with pytest.raises(Exception):
        page.goto()


class PythonPage(BasePage):
    "Page object for python.org"
    url = "https://www.python.org"
    def isCurrentPage(self):
        "Implements abstract method"
        return self.driver.get_title() == "Welcome to Python.org"

def test_goto_works():
    "Assert goto() and isCurrentPage() work if well-defined in class definition"
    mockdriver = Mock()
    page = PythonPage(mockdriver, 'Python Homepage')
    page.goto()
    mockdriver.get.assert_called_with("https://www.python.org")
