import base64
import os
import random
import threading
import time
from tkinter import *
import ico

import pyautogui

e = threading.Event()
e2 = threading.Event()

def printInfo():
    global quit
    quit['state'] = 'disabled'

    global run
    run['state'] = 'disabled'
    second = int(entry1.get())
    print(str(second))
    thread = threading.Thread(target=moveMouse, args=(second, ))
    thread.start()

    if entry2.get() != None and entry2.get() != '':
        countDownSecond = int(entry2.get()) * 60
        threadCountDown = threading.Thread(target=countDownFun, args=(countDownSecond,))
        threadCountDown.start()
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
        e2.set()
        quit['state'] = 'normal'
        run['state'] = 'normal'
    except KeyboardInterrupt as  e:
        print('log' + str(e))

def countDownFun(countDownSecond):
    global e2
    e2 = threading.Event()
    res = e2.wait(timeout = countDownSecond)
    if not res:
        # 计时到了
        # global e
        e.set()
    pass

def stopWait():
    e.set()

myWindow = Tk()
myWindow.title('keep V2.0')
tmp = open('tmp.ico', 'wb+')
tmp.write(base64.b64decode(ico.img))
tmp.close()
myWindow.iconbitmap('tmp.ico')
os.remove('tmp.ico')
#标签控件布局
Label(myWindow, text="interval:").grid(row=0)
# Label(myWindow, text="output").grid(row=1)
#Entry控件布局
entry1=Entry(myWindow)
# entry2=Entry(myWindow)
entry1.grid(row=0, column=1)
Label(myWindow, text="（秒）").grid(row=0, column=2)
# entry2.grid(row=1, column=1)

#标签控件布局
Label(myWindow, text="countdown:").grid(row=1)
# Label(myWindow, text="output").grid(row=1)
#Entry控件布局
entry2=Entry(myWindow)
# entry2=Entry(myWindow)
entry2.grid(row=1, column=1)
Label(myWindow, text="（分钟）").grid(row=1, column=2)


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
