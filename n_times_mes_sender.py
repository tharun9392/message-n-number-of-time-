import pyautogui as pg
import time
import random

animals=['NANNA','oyeeeeeeeeeeee','cheee','bujjiii kondaa','corryyyyyyyyy' ,'oseyyy','bujjiii nannaaa','hieee','nannnnnnaaaaaaa']

time.sleep(8)

for i in range(200):
    a=random.choice(animals)
    pg.write(f" {a}")
    pg.press('enter')