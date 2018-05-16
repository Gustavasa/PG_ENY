
import pyautogui as pg, os, sys, time
pg.FAILSAFE = False
pg.hotkey('winleft')

pg.typewrite('shell\n')
time.sleep(2)


while True:

    pg.typewrite('shutdown -s\n')
    time.sleep(1)

