import win32clipboard as clip
import pyautogui as pag
import time

print('Close this window in case of emergency')

clip.OpenClipboard()
data = clip.GetClipboardData()
clip.CloseClipboard()

data = data.replace('\n', ' ')
data = data.replace('\r', ' ')
data = data.split()

for i in data:
    time.sleep(0.40)
    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardText(i)
    clip.CloseClipboard()

    time.sleep(1)

    pag.hotkey('alt', 'shift', 'y')
    time.sleep(10)
