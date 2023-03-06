import base64
import os
import random
import threading
from tkinter import *
import ico

import pyautogui

e = threading.Event()

def printInfo():
    global quit
    quit['state'] = 'disabled'

    global run
    run['state'] = 'disabled'
    second = int(entry1.get())
    print(str(second))
    thread = threading.Thread(target=moveMouse, args=(second, ))
    thread.start()
    # moveMouse(second)
    print('sucess')


def moveMouse(t):
    try:
        while True:
            try:
                print('loop start')
                x = random.randint(-300, 300)
                y = random.randint(-300, 300)
                pyautogui.FAILSAFE = False
                # pyautogui.moveRel(x, y, duration=1)
                pyautogui.press('ctrl')

                global e
                e = threading.Event()
                res = e.wait(timeout= t)
                print(str(res))
                if res:
                    break

                # time.sleep(t)
            except pyautogui.FailSafeException:
                print('Failed')

        print('break')
        quit['state'] = 'normal'
        run['state'] = 'normal'
    except KeyboardInterrupt as  e:
        print('log' + str(e))

def stopWait():
    e.set()

myWindow = Tk()
myWindow.title('keep active')
tmp = open('tmp.ico', 'wb+')
tmp.write(base64.b64decode(ico.img))
tmp.close()
myWindow.iconbitmap('tmp.ico')
os.remove('tmp.ico')
#标签控件布局
Label(myWindow, text="time").grid(row=0)
# Label(myWindow, text="output").grid(row=1)
#Entry控件布局
entry1=Entry(myWindow)
# entry2=Entry(myWindow)
entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)
#Quit按钮退出；Run按钮打印计算结果

global quit
quit = Button(myWindow, text='Quit', command=myWindow.quit)
quit.grid(row=2, column=0, sticky=W, padx=5, pady=5)

global run
run = Button(myWindow, text='Run', command=printInfo)
run.grid(row=2, column=1, sticky=W, padx=5, pady=5)
stop = Button(myWindow, text='Stop', command=stopWait)
stop.grid(row=2, column=2, sticky=W, padx=5, pady=5)
#进入消息循环
myWindow.mainloop()


# try:
#     while True:
#         try:
#             x = random.randint(-300, 300)
#             y = random.randint(-300, 300)
#             pyautogui.FAILSAFE = False
#             pyautogui.moveRel(x, y)
#             time.sleep(1000)
#         except pyautogui.FailSafeException:
#             print('Failed')
# except KeyboardInterrupt as  e:
#     print('log' + str(e))
