"""Methods to handle waiting for a condition to be true"""
from time import sleep
from typing import Callable


def wait_until(
        condition_function: Callable[[], bool],
        timeout_seconds: float=5,
        polling_frequency_seconds: float=0.5) -> None:

    time_waited = 0
    while not condition_function():
        sleep(polling_frequency_seconds)
        time_waited += polling_frequency_seconds
