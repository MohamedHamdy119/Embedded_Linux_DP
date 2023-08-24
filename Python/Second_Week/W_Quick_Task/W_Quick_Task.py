#!/usr/bin/python3

import keyboard
import pyperclip

stored_text = ""

def on_key_event(event):
    global stored_text
    if event.event_type == "down" and event.name == "c" and keyboard.is_pressed("ctrl"):
        stored_text = pyperclip.paste()

keyboard.hook(on_key_event)

def append_to_notes():
    global stored_text
    with open("notes.txt", "a") as file:
        file.write(stored_text + "\n")
    print("Stored text appended to notes.txt.")

keyboard.add_hotkey("alt+shift+s", append_to_notes)

print("Clipboard monitoring started. Press 'Alt+Shift+S' to append stored text to notes.txt.")

keyboard.wait("esc")