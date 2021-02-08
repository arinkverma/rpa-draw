
import pyautogui as pgui
import time
from logger import logger


class RPA(object):

    @classmethod
    def waitForWindow(cls, title, retries=60):
        title_found = None
        for i in range(retries):
            title_found = pgui.getActiveWindow() and pgui.getActiveWindow().title
            if title_found and title_found.lower() == title.lower():
                logger.write("window_check opened: [{}]".format(title))
                time.sleep(1.0)
                return True
            time.sleep(1.0)
        raise Exception(u"Can't find window with title={}. Title found={}".format(title, title_found))

    @classmethod
    def hotkey(cls, command, delay=1, **kwargs):
        logger.write('hotkey: [{}]'.format(command))
        pgui.hotkey(*command)
        time.sleep(delay)

    @classmethod
    def typewrite(cls, command, delay=1, **kwargs):
        logger.write('typewrite: [{}]'.format(command))
        pgui.typewrite(command, **kwargs)
        time.sleep(delay)

    @classmethod
    def dragTo(cls, x, y):
        logger.write('dragTo: [{}, {}]'.format(x, y))
        pgui.dragTo(x, y, button='left')

    @classmethod
    def moveTo(cls, x, y):
        logger.write('moveTo: [{}, {}]'.format(x, y))
        pgui.moveTo(x, y)