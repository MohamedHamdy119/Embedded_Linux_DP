#!/usr/bin/python3
import pyautogui,time

#Using “Pyautogui” to open Emails and change Emails from unread to read

pyautogui.hotkey('win')
time.sleep(1)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.hotkey('ctrl','t')
time.sleep(1)
pyautogui.write('https://mail.google.com/')
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(4)
pyautogui.hotkey('*','a')
time.sleep(1)
pyautogui.hotkey('shift','i')
time.sleep(1)