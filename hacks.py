import pyautogui as pg
import time
i=0
while i<10:
    
    pg.click(901, 35, 1)
    pg.typewrite('gmail\n', .1)
    pg.moveTo(825, 256, 1)
    pg.click(825, 256, 1)
    pg.moveTo(750, 238, 4)
    pg.PAUSE = 3
    pg.click(750, 238, 1)

    pg.typewrite('srosenfeld@gcds.net', .1)
    pg.moveTo(934, 702, .1)
    pg.click(934, 702, 1)
    pg.PAUSE = 3
    pg.moveTo(1095, 170, .1)
    pg.click(1095, 170, 1)
    pg.moveTo(1066, 29, .1)
    pg.click(1066, 29, 1)
    i = i+1
