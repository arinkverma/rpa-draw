from rpa import RPA
from logger import logger
import subprocess
import pyautogui as pgui


class PaintApp():
    def __init__(self):
        logger.write('PaintApp init')
        self.process = None

    def __enter__(self):
        self.process = subprocess.Popen("C:\\Windows\\system32\\mspaint.exe")
        logger.write('PaintApp started')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        logger.write('PaintApp exited')
        self.process.kill()

    def selectBrush(self):
        RPA.hotkey(('alt', 'h'))
        RPA.hotkey(('alt', 'b'))
        RPA.hotkey(('enter',))

    def drawShape(self):
        x, y, length = 100, 200, 400
        RPA.moveTo(x, y)
        i = 0
        sides = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while length > 0:
            x += length * sides[i][0]
            y += length * sides[i][1]
            RPA.dragTo(x, y)
            length -= 5
            i = (i+1) % 4

    def saveImage(self, fileName):
        RPA.hotkey(('ctrl', 's'))
        RPA.waitForWindow(title="Save As")
        RPA.typewrite(fileName)
        RPA.hotkey(('alt', 's'))
