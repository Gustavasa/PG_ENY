import pyautogui as pg, os, sys, time
HelloFile = open('Hello.py', 'w')
HelloFile.write(
"""
import pyautogui as pg, os, sys, time
pg.hotkey('winleft')
pg.typewrite('shell\\n')
pg.typewrite('shutdown -s')



"""
)
HelloFile.close()

import Hello.py
