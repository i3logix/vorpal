"""
Package: Base
WebDriver Factory class implementation.
Creates a driver instance based on various browser configurations.
"""
from selenium import webdriver
from .custom_selenium_driver import CustomSeleniumDriver

class WebDriverFactory:
    
    def __init__(self, browser, base_url, webdriver = webdriver):
        """
        Initialize WebDriverFactory class.
        :param browser: specified browser.
        :param base_url: entry page URL
        """
        self.browser = browser
        self.base_url = base_url
        self.webdriver = webdriver

    def get_webdriver_instance(self, waiting_time=5) -> CustomSeleniumDriver:
        """
        Get WebDriver Instance based on the browser configuration.
        :param waiting_time: Implicit wait time for all elements on a web page.
        :return: Webdriver instance.
        """

        if self.browser == "firefox":
            driver = self.webdriver.Firefox()
        elif self.browser == "IE":
            driver = self.webdriver.Ie()
        else:
            driver = self.webdriver.Chrome()
            driver.set_window_size(1920, 1080)

        driver.implicitly_wait(waiting_time)
        driver.maximize_window()
        driver.get(self.base_url)

        return CustomSeleniumDriver(driver, implicit_wait=waiting_time)
