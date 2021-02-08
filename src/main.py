import os
import time
import shutil
from rpa import RPA
from paintApp import PaintApp


if __name__ == '__main__':
    time.sleep(10)
    with PaintApp() as app:
        RPA.waitForWindow(title="Untitled - Paint")
        app.selectBrush()
        app.drawShape()
        fileName = '101010.png'
        app.saveImage(fileName)
        RPA.waitForWindow(title="{} - Paint".format(fileName))
        RPA.hotkey(('alt', 'f'))
        RPA.hotkey(('alt', 'x'))
        shutil.move(
            os.path.join("C:\\", "Users", "vagrant", "Pictures", "101010.png"),
            os.path.join("C:\\", "Users", "vagrant", "Workplace", "rpa-draw", "101010.png"),
        )
