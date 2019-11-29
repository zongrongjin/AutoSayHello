from event import *
from settings import *
from time import sleep, time
from random import random


print('请在三秒内把你的鼠标放在输入框位置')
sleep(3)
x, y = get_mouse_position()

if USE_ENTER:
    print('获取鼠标位置成功，请返回相应的聊天界面，即将开始自动发送(移动鼠标停止发送)')
    sleep(WAIT_TIME)
    end = int(time()) + AUTO_SAY_HELLO_TIME
    now = int(time())
    x1, y1 = x, y
    count = 1
    while now < end and x1 == x and y1 == y:
        mouse_click(x, y)
        set_text()
        ctrl_v()
        tap_enter()
        sleep(DELAY_TIME + random())
        now = int(time())
        x1, y1 = get_mouse_position()
        count += 1
else:
    print('获取鼠标位置成功，请将三秒内将鼠标放到发送键位置')
    sleep(3)
    send_x, send_y = get_mouse_position()
    print('获取发送位置成功，请返回相应的聊天界面，即将开始自动发送(移动鼠标停止发送)')
    sleep(WAIT_TIME)
    end = int(time()) + AUTO_SAY_HELLO_TIME
    now = int(time())
    x1, y1 = x, y
    count = 1
    while now < end and ((x1 == x and y1 == y) or (x1 == send_x and y1 == send_y)):
        mouse_click(x, y)
        set_text()
        ctrl_v()
        mouse_click(send_x, send_y)
        sleep(DELAY_TIME + random())
        now = int(time())
        x1, y1 = get_mouse_position()
        count += 1