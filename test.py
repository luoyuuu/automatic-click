import pyautogui
import time
def mouse_click(img,sechdul_time) :
    #循环查看屏幕上匹配的图片
    while 1==1 :
        if pyautogui.locateCenterOnScreen(img,confidence = 0.8) :
            x, y = pyautogui.locateCenterOnScreen(img, confidence=0.8)
            pyautogui.moveTo(x, y)
            break
        else :
            continue
    #循环查看时间，当现实操作系统上的时间到达预设时间的时候，自动执行点击命令
    #如果预设时间小于现实时间，则直接跳出，并打印超时
    while 1 == 1 :
        current_time = time.strftime("%H:%M")
        if current_time == schedule_time :
            pyautogui.click()
            return
        if current_time > schedule_time :
            print('超时')
            return False
        else :
            continue
img =  r'图片的路径'
schedule_time = '点击的时间'

mouse_click(img, schedule_time)


