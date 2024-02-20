# import pyautogui

# pyautogui.keyDown('j')
# pyautogui.keyDown('a')
# pyautogui.keyDown('y')

from PIL import Image,ImageGrab
from numpy import imag

def takescr():
    image=ImageGrab.grab()
    image.show()

takescr()