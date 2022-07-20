import json
import tensorflow as tf
import os
import numpy as np
import requests
import cv2
import pyautogui
import time
import win32api, win32con
from pynput.keyboard import Key, Controller

headers = {"content-type": "application/json"}
axeUsage = 0

def takeScreenshot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    image = image[465:615, 885:1035]
    cv2.imwrite("image.png", image)
    image = tf.keras.utils.img_to_array(tf.keras.utils.load_img("C:\Projects\TL\scripts\image.png", target_size=(150, 150))) / 255.
    image = image.astype('float16')
    image = image[np.newaxis, :, :, :]
    return image

def getPrediction(imageToPred):
    data = json.dumps({"signature_name": "serving_default", "instances": imageToPred.tolist()})
    json_response = requests.post('http://172.18.189.216:9000/v1/models/tlCLassifier:predict', data=data, headers=headers)
    prediction = json.loads(json_response.text)['predictions']
    if prediction[0][0] > prediction[0][1] and prediction[0][0] > prediction[0][2]:
        return "none"
    elif prediction[0][1] > prediction[0][0] and prediction[0][1] > prediction[0][2]:
        return "rock"
    elif prediction[0][2] > prediction[0][0] and prediction[0][2] > prediction[0][1]:
        return "tree"
    else:
        return "none"

def getDistance(imageToPred):
    data = json.dumps({"signature_name": "serving_default", "instances": imageToPred.tolist()})
    json_response = requests.post('http://172.18.189.216:9001/v1/models/tlCLassifier2:predict', data=data, headers=headers)
    prediction = json.loads(json_response.text)['predictions']
    if prediction[0][0] > prediction[0][1] and prediction[0][0] > prediction[0][2]:
        return "close"
    elif prediction[0][1] > prediction[0][0] and prediction[0][1] > prediction[0][2]:
        return "far"
    elif prediction[0][2] > prediction[0][0] and prediction[0][2] > prediction[0][1]:
        return "none"
    else:
        return "none"

def moveMouse(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,x,y)

def panMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,10,0) #1180,670 full screen 570 - 90 degrees

def downMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,0,20)

def upMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,0,-20)

def centerMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,0,-120)

def absCenterMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,32768,32768,0,0)

def scrollIn():
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,100,0)

def scrollOut():
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-100,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-100,0)

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)


def moveForwardShort():
    Controller().press('w')
    time.sleep(0.25)
    Controller().release('w')

def moveForwardLong():
    Controller().press(Key.shift_l)
    Controller().press('w')
    time.sleep(0.4)
    Controller().release(Key.shift_l)
    Controller().release('w')

def inventoryOpen():
    Controller().press('g')
    time.sleep(0.025)
    Controller().release('g')

def press1():
    Controller().press('1')
    time.sleep(0.025)
    Controller().release('1')

def axeEquip():
    global axeUsage
    if axeUsage > 60 :
        scrollOut()
        time.sleep(0.2)
        inventoryOpen()
        time.sleep(0.2)
        absCenterMouse()
        time.sleep(0.2)
        click()
        time.sleep(0.2)
        moveMouse(40,25)
        time.sleep(0.2)
        click()
        time.sleep(0.2)
        absCenterMouse()
        time.sleep(0.2)
        inventoryOpen()
        time.sleep(0.2)
        scrollIn() 
    else :
        press1()

def axeDequip():
    press1()
    time.sleep(0.3)
    scrollIn()

def chop():
    click()
    time.sleep(1)
    click()
    time.sleep(1)
    click()
    time.sleep(1)
    click()
    time.sleep(1)
    click()
    time.sleep(1)
    click()
    time.sleep(1)
    click()
    time.sleep(1)

def checkTree():
    image = takeScreenshot()
    sceneStatus = getPrediction(image)
    distanceStatus = getDistance(image)
    return sceneStatus, distanceStatus

def scanArea():
    scenestat = False
    while scenestat != True :
        Controller().press('w')
        a,b = checkTree()
        if a == "tree" and (b == "close" or b == "far"):
            Controller().release('w')
            walkToTree(b)
            scenestat = True
            break
        else:
            Controller().release('w')
            panMouse()

def walkToTree(distance):
    if distance == "close":
        moveForwardShort()
        obliterateTree()
    elif distance == "far":
        moveForwardLong()
        moveMouse(-10,0)
        a,b = checkTree()
        if a == "tree" and b == "close":
            moveForwardShort()
            obliterateTree()
        elif a == "tree" and b =="far":
            moveForwardLong()
            scanArea() #scan to check how far the tree is
        else:
            scanArea() #no tree what the...


def obliterateTree():
    moveMouse(12,0)
    axeEquip()
    Controller().press('s')
    time.sleep(0.15)
    Controller().release('s')
    global axeUsage
    status = False
    while status == False:
        chop()
        axeUsage = axeUsage + 1
        time.sleep(0.3)
        moveMouse(-220,0)
        time.sleep(0.2)
        a,b = checkTree()
        if a != "tree":
            axeDequip()
            time.sleep(0.5)
            a,b = checkTree()
            if a != "tree":
                moveMouse(220,0)
                status = True
                scanArea()
                break
            else:
                axeEquip()
        else:
            moveMouse(260,0)

print("starting")
time.sleep(5)
scanArea()