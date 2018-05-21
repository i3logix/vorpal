"""
Package: Base
WebDriver Factory class implementation.
Creates a driver instance based on various browser configurations.
"""
from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser, base_url):
        """
        Initialize WebDriverFactory class.
        :param browser: specified browser.
        :param base_url: entry page URL
        """
        self.browser = browser
        self.base_url = base_url

    def get_webdriver_instance(self, waiting_time=5) -> webdriver:
        """
        Get WebDriver Instance based on the browser configuration.
        :param waiting_time: Implicit wait time for all elements on a web page.
        :return: Webdriver instance.
        """

        if self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "IE":
            driver = webdriver.Ie()
        else:
            driver = webdriver.Chrome()
            driver.set_window_size(1920, 1080)

        driver.implicitly_wait(waiting_time)
        driver.maximize_window()
        driver.get(self.base_url)

        return driver
