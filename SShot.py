
import pyautogui
import time
import os

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

year=2020
month=1
print('Press Ctrl-C to quit.')

time.sleep(5)
path='./Captures/dayByday'  #+str(year)
folder=path+'/'
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

try:
    for month in range(323,350):

        pyautogui.moveTo(1170, 110, duration=0.25)
        x, y = pyautogui.position()
        pyautogui.click(x,y)

        time.sleep(2)
        dosya=folder+str(month)+'.jpg'
        im2 = pyautogui.screenshot(dosya,region=(0,0, 1920, 1025))
except KeyboardInterrupt:
    print('\ninterupted.')    


print('\nDone.')
