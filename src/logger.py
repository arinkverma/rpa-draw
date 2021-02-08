import os
from os.path import dirname, abspath
from datetime import datetime

ROOT_PATH = dirname(abspath(__file__))


class Logger(object):

    def __init__(self):
        self.log = open(os.path.join(ROOT_PATH, "run.log"), 'a')

    def write(self, message=''):
        message = '{} -- {}'.format(datetime.now(), message)
        message = message + '\n'
        self.log.write(message)
        self.log.flush()
        os.fsync(self.log)


logger = Logger()
