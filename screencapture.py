from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import win32gui
from object_recognition import searchInImage

# width = GetSystemMetrics(0)
# height = GetSystemMetrics(1)
toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

def gen_frames():
    while True:
        win32gui.EnumWindows(enum_cb, toplist)
        window = [(hwnd, title) for hwnd, title in winlist if 'Rivals of Aether' in title]
        window = window[0]
        hwnd = window[0]
        bbox = win32gui.GetWindowRect(hwnd)
        
        img = ImageGrab.grab(bbox)
        img_np = np.array(img)
        oldframe = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        frame = searchInImage(oldframe)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')