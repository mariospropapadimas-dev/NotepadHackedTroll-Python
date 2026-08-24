import pyautogui as p
import time
import os
import webbrowser
import ctypes
import winsound

REAL_SHUTDOWN = False  # set True to actually shut down the PC at the end

ctypes.windll.user32.MessageBoxW(0, "Critical System Failure Detected!", "Windows Security Alert", 0x10)

p.hotkey( "win" , "r")
p.write("cmd")
p.press("enter")
time.sleep(1)
p.write("color 02")
p.press("enter")
time.sleep(1)
p.write("dir/s")
p.press("enter")
time.sleep(5)

webbrowser.open_new_tab("https://youtu.be/xvFZjo5PgG0?si=8aTfPhxDtyrYZ5Q6")

p.hotkey("win" , "r")
time.sleep(1)
p.write("notepad")
p.press("enter")
time.sleep(1)
p.write("YOU HAVE BEEN HACKED PAY MONEY!!! \n")
p.write("Your pc will shut down in \n")
time.sleep(1)

for n in ("3", "2", "1"):
    p.write(n + "\n")
    winsound.Beep(1000, 300)
    time.sleep(1)

if REAL_SHUTDOWN:
    os.system("shutdown /s /t 1")
else:
    p.write("\nJust kidding! \U0001F604 You have NOT been hacked.\n", interval=0.08)
