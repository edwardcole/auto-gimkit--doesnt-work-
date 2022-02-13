import pyautogui
import time
from multiprocessing import Process

def Check():
    marsh = pyautogui.locateOnScreen('marsh.png', confidence=0.9)
    if marsh != None:
        pyautogui.click(marsh)
def Continue():
    time.sleep(0.1)
    pyautogui.click(x=968, y=911)
while True:
    Check()
    Continue()
    