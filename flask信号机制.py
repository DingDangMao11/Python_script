from flask import Flask
from blinker import Namespace

# Namespace : 命名空间
# 1. 定义信号
zlspace = Namespace()
fire_signal = zlspace.signal('fire')

#2. 监听信号
def fire_bullet(sender):
    print(sender)
    print('start fire bullet')
fire_signal.connect(fire_bullet)

#3. 发送一个信号
fire_signal.send()
