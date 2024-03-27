import pyautogui

import keyboard
import time

import tkinter as tk

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.destroy()

times = 0


def press_keys():
    # 模拟按下w键
    keyboard.press('w')
    time.sleep(5)
    keyboard.release('w')

    # 模拟按下s键
    keyboard.press('s')
    time.sleep(5)
    keyboard.release('s')

    # 模拟按下w键
    keyboard.press('a')
    time.sleep(5)
    keyboard.release('a')

    # 模拟按下s键
    keyboard.press('d')
    time.sleep(5)
    keyboard.release('d')

    keyboard.press('space')
    time.sleep(0.1)
    keyboard.release('space')


while times < 360:
    time.sleep(0.1)
    pyautogui.moveTo(round((2000/3840) * width), round((2050/2160) * height), duration=0)
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(1)
    press_keys()
    time.sleep(0.1)
    pyautogui.moveTo(round((3200/3840) * width), round((320/2160) * height), duration=0)
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.moveTo(round((2000/3840) * width), round((1900/2160) * height), duration=0)
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(1)
    times += 1
