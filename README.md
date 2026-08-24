# NotepadHackedTroll-Python
A simple Python prank script that simulates a fake "hacker attack" by opening Command Prompt, displaying scary messages, rickrolling the victim, and shutting down the PC. Made for educational and entertainment purposes only.

# Fake Hacker Prank
<img width="1919" height="1034" alt="Στιγμιότυπο οθόνης 2026-06-08 174549" src="https://github.com/user-attachments/assets/dce714dd-e737-450c-a89e-b63601b9b0e7" />

A simple Python prank script that creates the illusion of a computer being hacked.

## Features

* Pops up a fake Windows error message for an instant jump-scare
* Opens Command Prompt automatically
* Changes CMD text color to green
* Runs a fake directory scan
* Opens a surprise video (Rickroll)
* Creates a scary Notepad message
* Displays a fake countdown with dramatic beeps
* Ends with a typed-out "Just kidding!" reveal — the PC is safe by default
* Real shutdown is available too, behind a single on/off switch

## Requirements

```bash
pip install pyautogui
```

`ctypes` and `winsound` are used for the popup and beeps, but both are built into Python on Windows — no extra install needed.

## Usage

Run the script:

```bash
python main.py
```

The script will:

1. Show a fake "Critical System Failure" popup
2. Open Command Prompt
3. Execute fake "hacker-looking" commands
4. Open a surprise video
5. Display a fake warning message
6. Count down from 3, with a beep each second
7. Type out a "Just kidding!" message (or shut down the PC, if enabled)

## Warning

This project is intended for educational and entertainment purposes only.

Do not run this on computers without the owner's permission.

By default the script does **not** actually shut down the PC — it ends with a harmless "Just kidding!" message typed into Notepad. If you want the original real-shutdown behavior, open `main.py` and set `REAL_SHUTDOWN = True` at the top of the file. With that flag on, the script *will* shut down the system automatically after execution.

## Disclaimer

The author is not responsible for any misuse of this project. Use responsibly and only as a harmless prank among friends.

## Preview

```
YOU HAVE BEEN HACKED PAY MONEY!!!

Your pc will shut down in

3
2
1

Just kidding! 😄 You have NOT been hacked.
```

Have fun and don't scare your friends too much. 😈
