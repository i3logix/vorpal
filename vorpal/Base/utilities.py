"""
Package: Utilities
Implementation of different utility methods.
Provides functionality of loggin all messages.
"""

import logging
import inspect
from pathlib import Path


class Utilities:

    @staticmethod
    def custom_logger(log_level, log_name=None):
        """
        Create a custom logger with custom.log
        Provides functionality of loggin all messages.
        :param log_level: Default log level for specific log.
        :param log_name: Specific name of the log. 
        """

        logger_name = inspect.stack()[1][3]

        my_path = str(Path(__file__).parents[1])
        path = my_path + "/Logs/"

        logger = logging.getLogger(path + logger_name) if log_name is None else logging.getLogger(path + log_name)
        logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler(path + 'automation.log', mode='a') if log_name is None else logging.FileHandler('{0}.log'.format(log_name))
        handler.setLevel(log_level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S.%p')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger
