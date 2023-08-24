#!/usr/bin/python3

import pyautogui
import time

pyautogui.hotkey('win')
time.sleep(1)
pyautogui.write('visual')
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.hotkey('ctrl','shift','x')
time.sleep(1)

#**************************************************
#install function

def Install_Ext (ser=''):

   Find_Photo = None
   while Find_Photo is None :
      Find_Photo = pyautogui.locateOnScreen('EXT.png',confidence=0.9)

   if Find_Photo is not None :
      pyautogui.moveTo(Find_Photo[0]+150,Find_Photo[1]+60)
      time.sleep(0.5)

   time.sleep(0.5)
   pyautogui.click(clicks=3)
   time.sleep(0.5)
   pyautogui.hotkey('backspace')
   time.sleep(1)
   
   pyautogui.write(ser)
   time.sleep(2)
   Find_Photo = None
   while Find_Photo is None :
      Find_Photo = pyautogui.locateOnScreen('install.png',confidence=0.8)
      time.sleep(1)

   if Find_Photo is not None :
      pyautogui.moveTo(Find_Photo[0]+5,Find_Photo[1]+5)
      time.sleep(0.5)

   time.sleep(1)
   pyautogui.click()
   time.sleep(6)


#**************************************************
#install clangd from extension
Install_Ext('clangd')

#**************************************************
#install c++ testmate  from extension
Install_Ext('c++ testmate')

#**************************************************
#install c++ helper  from extension
Install_Ext('c++ helper')

#**************************************************
#install cmake  from extension
Install_Ext('cmake')

#**************************************************
#install cmake tools  from extension
Install_Ext('cmake tools')










