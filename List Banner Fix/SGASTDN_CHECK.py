import win32clipboard as clip
import pyautogui as pag
import time

print('Close this window in case of emergency')

clip.OpenClipboard()
gNumbers = clip.GetClipboardData()
clip.CloseClipboard()

gNumbers = gNumbers.replace('\n', ' ')
gNumbers = gNumbers.replace('\r', ' ')
gNumbers = gNumbers.split()

for i in gNumbers:
    # Set the G# into the clipboard
    time.sleep(0.5)
    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardText(i)
    clip.CloseClipboard()

    time.sleep(1)

    #Run the AHK script to type the G# into Banner
    pag.hotkey('alt', 'shift', 'y')
    time.sleep(5)
