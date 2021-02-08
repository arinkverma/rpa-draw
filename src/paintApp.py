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
        side = 400
        x, y = 100, 200
        RPA.moveTo(x, y)
        while side > 0:
            side -= 5
            x += side
            RPA.dragTo(x, y)
            side -= 5
            y += side
            RPA.dragTo(x, y)
            side -= 5
            x -= side
            RPA.dragTo(x, y)
            side -= 5
            y -= side
            RPA.dragTo(x, y)

    def saveImage(self, fileName):
        RPA.hotkey(('ctrl', 's'))
        RPA.waitForWindow(title="Save As")
        RPA.typewrite(fileName)
        RPA.hotkey(('alt', 's'))
