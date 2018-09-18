import win32clipboard as clip
import pyautogui as pag
import time

print('Getting program ready...')

time.sleep(2)
print('\nHightlight and copy the G#s')
clip.OpenClipboard()
gNum = clip.GetClipboardData()
clip.CloseClipboard()

time.sleep(2)
print('\n Highlight and copy the FICE codes')
clip.OpenClipboard()
fCode = clip.GetClipboardData()
clip.CloseClipboard()




for i in gNum:
    time.sleep(0.40)
    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardText(i)
    clip.CloseClipboard()

    time.sleep(1)

    pag.hotkey('alt', 'shift', 'y')
    time.sleep(5)
