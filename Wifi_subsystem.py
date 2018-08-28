# -*- coding: utf-8 -*-
# 需要先安装pywin32模块
#https://docs.microsoft.com/zh-cn/windows/desktop/inputdev/about-mouse-input
import win32gui
import win32con
import win32api
import win32clipboard as w
from ctypes import *
import time
import os
import re
import time
import subprocess


VK_CODE = {
    'backspace': 0x08,
    'tab': 0x09,
    'clear': 0x0C,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'pause': 0x13,
    'caps_lock': 0x14,
    'esc': 0x1B,
    'spacebar': 0x20,
    'page_up': 0x21,
    'page_down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
    'select': 0x29,
    'print': 0x2A,
    'execute': 0x2B,
    'print_screen': 0x2C,
    'ins': 0x2D,
    'del': 0x2E,
    'help': 0x2F,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'a': 0x41,
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,
    'numpad_0': 0x60,
    'numpad_1': 0x61,
    'numpad_2': 0x62,
    'numpad_3': 0x63,
    'numpad_4': 0x64,
    'numpad_5': 0x65,
    'numpad_6': 0x66,
    'numpad_7': 0x67,
    'numpad_8': 0x68,
    'numpad_9': 0x69,
    'multiply_key': 0x6A,
    'add_key': 0x6B,
    'separator_key': 0x6C,
    'subtract_key': 0x6D,
    'decimal_key': 0x6E,
    'divide_key': 0x6F,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
    'F13': 0x7C,
    'F14': 0x7D,
    'F15': 0x7E,
    'F16': 0x7F,
    'F17': 0x80,
    'F18': 0x81,
    'F19': 0x82,
    'F20': 0x83,
    'F21': 0x84,
    'F22': 0x85,
    'F23': 0x86,
    'F24': 0x87,
    'num_lock': 0x90,
    'scroll_lock': 0x91,
    'left_shift': 0xA0,
    'right_shift ': 0xA1,
    'left_control': 0xA2,
    'right_control': 0xA3,
    'left_menu': 0xA4,
    'right_menu': 0xA5,
    'browser_back': 0xA6,
    'browser_forward': 0xA7,
    'browser_refresh': 0xA8,
    'browser_stop': 0xA9,
    'browser_search': 0xAA,
    'browser_favorites': 0xAB,
    'browser_start_and_home': 0xAC,
    'volume_mute': 0xAD,
    'volume_Down': 0xAE,
    'volume_up': 0xAF,
    'next_track': 0xB0,
    'previous_track': 0xB1,
    'stop_media': 0xB2,
    'play/pause_media': 0xB3,
    'start_mail': 0xB4,
    'select_media': 0xB5,
    'start_application_1': 0xB6,
    'start_application_2': 0xB7,
    'attn_key': 0xF6,
    'crsel_key': 0xF7,
    'exsel_key': 0xF8,
    'play_key': 0xFA,
    'zoom_key': 0xFB,
    'clear_key': 0xFE,
    '+': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    '`': 0xC0,
    ';': 0xBA,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE,
    '`': 0xC0}
class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


def get_mouse_point():
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    return int(po.x), int(po.y)


def mouse_click(x=None, y=None):
    if not x is None and not y is None:
        mouse_move(x, y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def mouse_dclick(x=None, y=None):
    if not x is None and not y is None:
        mouse_move(x, y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def mouse_move(x, y):
    windll.user32.SetCursorPos(x, y)


def key_input(str=''):
    for c in str:
        win32api.keybd_event(VK_CODE[c], 0, 0, 0)
        win32api.keybd_event(VK_CODE[c], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.01)

#wifi 重启压力测试
def wifi_test():
    global wifiList
    wifiList = []
    for i in range(50):
        print "                   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                           "
        print "                   +                                                                   +                           "
        print "                   +              This is the " + str(i) + "循环                       +                           "
        print "                   +                                                                   +                           "
        print "                   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                           "
        p1 = (391, 65)
        handle = win32gui.FindWindow("Qt5QWindowIcon", None)
        # print handle
        rect = win32gui.GetWindowRect(handle)
        win32api.SetCursorPos((rect[0] + p1[0], rect[1] + p1[1]))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        str1 = "send"
        key_input(str1)
        # 模拟按下'shift+-'键,实现"_"下划线符号
        win32api.keybd_event(0x10, 0, 0, 0);
        win32api.keybd_event(0xBD, 0, 0, 0);
        win32api.keybd_event(109, 0, win32con.KEYEVENTF_KEYUP, 0);
        win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0);
        str2 = "data"
        key_input(str2)
        # 空格键
        time.sleep(4)
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        str3 = "75"
        key_input(str3)
        # 空格键
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        str4 = "37"
        key_input(str4)
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        str4 = "03"
        key_input(str4)
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        str5 = "176"
        key_input(str5)
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        str6 = "00"
        key_input(str6)
        qxdm = win32gui.FindWindow("Qt5QWindowIcon", None)
        win32gui.SendMessage(qxdm, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.SendMessage(qxdm, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        time.sleep(4)
        time.sleep(20)
        command = "adb shell ping -c 3 baidu.com"
        baidu_info=os.popen(command)
        baidu= baidu_info.readlines()
        print baidu
        if   baidu:
             print '      ++++++++++++++++++++++++++++++'
             print '      +++++++++WIFI可以上网++++++++++'
             print '      ++++++++++++++++++++++++++++++'
        else:
            print  "WIFI不可以上网"
    # 1.获取50次wifi的掉线日志信息
    shellcmd0 = " adb " + "shell \" dumpsys wifi | grep NETWORK_DISCONNECTION_EVENT \"  "
    wifi_discon = os.popen(shellcmd0).readlines()
    print len(wifi_discon)
    print "               +++++++++++++++++++++++++++++++++50次wifi的掉线日志信息++++++++++++++++++++++++++++++++++++++++++++++++++              "
    for i in wifi_discon:
        print wifi_discon
    print "               +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++              "
    # 3.根据wifi日志特性，循环倒数前50的日志
    global wifi_event
    wifi_event = []
    for j in range(len(wifi_discon) - 49, len(wifi_discon) - 1):
        # 4.倒数前50的日志列表分列
        print wifi_discon[j].split()
        wifi_split = wifi_discon[j].split()
        net_discon = wifi_split[2]
        # 5. wifi_event 放有 wifi_split[2]='NETWORK_DISCONNECTION_EVENT' ,循环50次应该有50次“NETWORK_DISCONNECTION_EVENT”
        wifi_event.append(net_discon)
    print "               ++++++++++++++++++++++++++++++++++倒数前50的日志列表分列信息+++++++++++++++++++++++++++++++++++++++++++++              "
    for m in wifi_event:
        print "----------->" + m
    print "               +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++              "

    shellcmd1 = " adb " + "shell \" dumpsys wifi | grep NETWORK_CONNECTION_EVENT \"  "
    wifi_con = os.popen(shellcmd1).readlines()
    print len(wifi_con)
    print "               +++++++++++++++++++++++++++++++++50次wifi的掉线日志信息++++++++++++++++++++++++++++++++++++++++++++++++++              "
    for i in wifi_con:
        print wifi_con
    print "               +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++              "
    # 3.根据wifi日志特性，循环倒数前50的日志
    global wifi_in_event
    wifi_in_event = []
    for j in range(len(wifi_con) - 49, len(wifi_con) - 1):
        # 4.倒数前50的日志列表分列
        print wifi_con[j].split()
        wifi_in_split = wifi_con[j].split()
        net_con = wifi_in_split[2]
        # 5. wifi_event 放有 wifi_split[2]='NETWORK_DISCONNECTION_EVENT' ,循环50次应该有50次“NETWORK_DISCONNECTION_EVENT”
        wifi_in_event.append(net_con)
    print "               ++++++++++++++++++++++++++++++++++倒数前50的日志列表分列信息+++++++++++++++++++++++++++++++++++++++++++++              "
    for sign_in in wifi_in_event:
        print "----------->" + sign_in
    print "               +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++              "
    if 'NETWORK_CONNECTION_EVENT' in wifi_in_event:
        if 'NETWORK_DISCONNECTION_EVENT' in wifi_event:
            print "                   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                           "
            print "                   +                                                                   +                           "
            print "                   +              Wifi reconnected 50 times successfully                                     +                           "
            print "                   +                                                                   +                           "
            print "                   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                           "
            print "                   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                           "
            print "                   +                                                                   +                           "
            print "                   +              Wifi dropped 50 tests successfully                                     +                           "
            print "                   +                                                                   +                           "
            print "                   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                           "
            print "                                              ++++++                                                               "
            print "                                              ++++++                                                               "
            print "                                              ++++++                                                               "
            print "                                              ++++++                                                               "
            print "                                               +++                                                                 "
            print "                                                +                                                                  "
            print "                   +++++++++++++++++++++++++++最终结果+++++++++++++++++++++++++                           "
            print "                   +                                                                   +                           "
            print "                   +              Wifi reconnected&dropped 50 times successfully                                     +                           "
            print "                   +                                                                   +                           "
            print "                   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                           "
    else:
        print "                   +++++++++++++++++++++++++++最终结果+++++++++++++++++++++++++                           "
        print "                   +                                                                   +                           "
        print "                   +              Wifi reconnected&dropped 50 times failly                                     +                           "
        print "                   +                                                                   +                           "
        print "                   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                           "

        # for i in wifi_disconnection:
    #      print  i
    # pout1 = subprocess.Popen(" adb "+ "shell \" dumpsys wifi | grep NETWORK_DISCONNECTION_EVENT\"  ", shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # wifi_disconnection = pout1.stdout.readlines()
    # print wifi_disconnection
    # 2.将掉线日志信息存放到一个列表中
    #

    # 1.打开文件
    # file_handle = open('wifi_info.xls', mode='w')
    # # 2.写入数据
    # for wifi in wifi_disconnection:
    #     file_handle.write(wifi)
    #     # 写入换行符
    #     # file_handle.write('\n')
    # # 3.关闭文件
    # file_handle.close()
        #NETWORK_DISCONNECTION_EVENT
        # if 'NETWORK_CONNECTION_EVENT,' in wifi_disconnection:
        #     print 'WIFI重启测试成功'
        # else:
        #     print 'WIFI重启测试失败'
        # command = "adb shell dumpsys wifi | grep NETWORK_CONNECTION_EVENT > data/local/tmp/ping.txt"
        # os.system(command)
        # #判断wifi是否掉线
        # while True:
        #      command = "adb shell ping -c 3 baidu.com > ping_out.txt"
        #      os.system(command)
        #      f = open('ping_out.txt', 'r')
        #      list=f.readlines()
        #      print list
        #      if len(list):
        #           print "WIFI还在线"
        #      else :
        #           print "++++++++++++++++++++++++++++++++++"
        #           print "+++++++    WIFI已经掉线     ++++++"
        #           print "++++++++++++++++++++++++++++++++++"
        #           shellcmd1 = "adb shell \" echo   '1'  >> /data/local/tmp/log.txt\" "
        #           os.system(shellcmd1)
        #           break
        # time.sleep(7)
        # #判断wifi是否连接


# LPASS subsystem 重启压力测试
def lpass_test():
    for i in range(50):
        print "This is the " + str(i) + "循环"
        p1 = (391, 65)
        handle = win32gui.FindWindow("Qt5QWindowIcon", None)
        # print handle
        rect = win32gui.GetWindowRect(handle)
        win32api.SetCursorPos((rect[0] + p1[0], rect[1] + p1[1]))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        str1 = "send"
        key_input(str1)
        # 模拟按下'shift+-'键,实现"_"下划线符号
        win32api.keybd_event(0x10, 0, 0, 0);
        win32api.keybd_event(0xBD, 0, 0, 0);
        win32api.keybd_event(109, 0, win32con.KEYEVENTF_KEYUP, 0);
        win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0);
        str2 = "data"
        key_input(str2)
        # 空格键
        time.sleep(4)
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        str3 = "75"
        key_input(str3)
        # 空格键
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        str4 = "37"
        key_input(str4)
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        str4 = "03"
        key_input(str4)
        win32api.keybd_event(0x20, 0, 0, 0);
        win32api.keybd_event(0x20, 0, 0, 0);
        str5 = "48"
        key_input(str5)
        qxdm = win32gui.FindWindow("Qt5QWindowIcon", None)
        win32gui.SendMessage(qxdm, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.SendMessage(qxdm, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        time.sleep(4)

if __name__ =='__main__':
    #首先重启手机

     wifi_test()
    # lpass_test()


