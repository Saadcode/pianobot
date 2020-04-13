import pyautogui as pyg
from mss import mss
import time

start_x = 468
start_y = 437

bbox = (start_x, start_y, start_x+300, start_y+1)

cord_x = [0, 100, 200, 290]

def start() :
  time.sleep(1)
  with mss() as ms :
    while True :  
      img = ms.grab(bbox)
      for cord in cord_x :
        if img.pixel(cord, 0)[0] < 100:
          pyg.click(start_x+cord, start_y)          
          break 

start()