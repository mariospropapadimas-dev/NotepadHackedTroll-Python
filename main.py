import pyautogui as p
import time
import os
import webbrowser

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
p.write("3\n")
time.sleep(1)
p.write("2\n")
time.sleep(1)
p.write("1\n")
time.sleep(1)
os.system("shutdown /s /t 1")
