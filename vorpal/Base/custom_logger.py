"""
Framework Logger class implementation.
Provides functionality of loggin all messages.
"""
import logging, logging.config, os


class LogFileHandler(logging.FileHandler):
    """ It helps to generate the Path to log file based on user configuration """

    def __init__(self, path, file_name, mode):
        if not os.path.exists(path):
            os.mkdir(path)
        super(LogFileHandler, self).__init__(path + "/" + file_name, mode)


class FrameworkLogger:
    @staticmethod
    def custom_logger(logger='main'):
        """ Create a custom logger """
        conf_path = os.path.dirname(os.path.realpath(__file__)) + '/conf/log.conf'
        logging.config.fileConfig(conf_path, disable_existing_loggers=False)
        logger = logging.getLogger(str(logger))
        return logger
