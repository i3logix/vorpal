"""
Package: Base
WebDriver Factory class implementation.
Creates a driver instance based on various browser configurations.
"""
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .custom_selenium_driver import CustomSeleniumDriver

class WebDriverFactory:
    
    def __init__(self, browser: str, base_url: str, webdriver = webdriver, remote: bool = False, remote_url: str = 'http://127.0.0.1:4444/wd/hub'):
        """
        Initialize WebDriverFactory class.
        :param browser: specified browser.
        :param base_url: entry page URL
        """
        self.browser = browser
        self.base_url = base_url
        self.webdriver = webdriver
        self.remote = remote
        self.remote_url = remote_url

        self.desired_capabilities: DesiredCapabilities = {
            'chrome': DesiredCapabilities.CHROME,
            'firefox': DesiredCapabilities.FIREFOX,
            'IE': DesiredCapabilities.INTERNETEXPLORER,
        }.get(browser, DesiredCapabilities.CHROME)

    def get_webdriver_instance(self, waiting_time: int = 5) -> CustomSeleniumDriver:
        """
        Get WebDriver Instance based on the browser configuration.
        :param waiting_time: Implicit wait time for all elements on a web page.
        :return: Webdriver instance.
        """
        if self.remote:
            driver = self.webdriver.Remote(
                command_executor=self.remote_url,
                desired_capabilities=self.desired_capabilities)
        else:
            if self.browser == "firefox":
                driver = self.webdriver.Firefox()
            elif self.browser == "IE":
                driver = self.webdriver.Ie()
            else:
                driver = self.webdriver.Chrome()
                driver.set_window_size(1920, 1080)

        driver.implicitly_wait(waiting_time)
        driver.get(self.base_url)

        return CustomSeleniumDriver(driver, implicit_wait=waiting_time)
