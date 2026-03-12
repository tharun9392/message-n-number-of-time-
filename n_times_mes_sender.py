import pyautogui as pg
import time
import random

animals=['hloo','oyeeeeeeeeeeee','hai','hai','hay' ,'yyy','yehaaa','hieee','aaaaaaa']

time.sleep(8)

for i in range(200):
    a=random.choice(animals)
    pg.write(f" {a}")
    pg.press('enter')
