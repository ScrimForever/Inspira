import datetime
import uuid

from pynput import mouse
import pyautogui
import os
import httpx

'''
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
'''


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        screenshot = pyautogui.screenshot()
        if os.name == 'nt':
            file = 'C:\\temp\\shot_{datetime.datetime.now().date()}.jpg'
            name = uuid.uuid4()
            screenshot.save(file)
            file = {'file': open(file, 'rb')}
            httpx.post(f'http://127.0.0.1:9999/screen/{name}/', files=file)
        else:
            pass


'''
def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
'''

# Collect events until released
with mouse.Listener(
        on_click=on_click
    ) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_click=on_click
    )

listener.start()
