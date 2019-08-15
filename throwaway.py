from pyautogui import typewrite, time, hotkey, PAUSE, press, FAILSAFE, moveTo, click, pixelMatchesColor, screenshot

FAILSAFE = True



print(screenshot().getpixel((480, 670)))

moveTo(450, 400, duration=2)
if pixelMatchesColor(450, 400, (255,108,64)):
    print("ORANGE")
    click()

time.sleep(1)
press('pgdn')

moveTo(480, 670, duration=2)
if pixelMatchesColor(480, 670, (20, 151, 255)):
    print("blue")
    click()

