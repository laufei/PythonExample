# coding: utf-8
__author__ = 'liufei'

import logging
class test:
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s - line:%(lineno)d] %(message)s')

    def printLog(self):
        logging.debug('This is debug message')
        logging.info('This is info message')
        logging.warning('This is warning message')

test().printLog()