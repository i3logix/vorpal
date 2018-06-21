from time import sleep
from selenium.common.exceptions import InvalidElementStateException, ElementNotVisibleException, \
    ElementNotInteractableException, ElementNotSelectableException, ElementClickInterceptedException

def retry_with_timeout(func):
    """Decorator to retry function every :action_increment seconds, up to action_timeout seconds"""
    def wrapped(self, *args, **kwargs):
        timeout = kwargs.get('action_timeout', 5) or 5
        increment = kwargs.get('action_increment', 0.5)
        total = 0
        while total < timeout:
            try:
                return func(self, *args, **kwargs)
            except (InvalidElementStateException,
                    ElementNotVisibleException,
                    ElementNotInteractableException,
                    ElementNotSelectableException,
                    ElementClickInterceptedException):
                sleep(increment)
                total += increment

    return wrapped
