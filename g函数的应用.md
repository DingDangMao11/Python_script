####  1. app.py
```
# encoding : utf-8
from flask import Flask,request,g
from blinker import Namespace
from signals import login_signal

# 定义一个登录的信号，以后用户登录进来以后
# 就发送一个登录信号吗，然后能够监听这个信号
# 再监听到这个信号以后，就记录当前这个用户的登录信息
# 用信号的方式，记录用户的登录信息

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/')
def login():
    #通过查询字符串的形式来传递username这个参数
    username = request.args.get('username')
    if username:
        # 3.发送信号
        g.username = username
        login_signal.send()
        return '登陆成功！'
    else:
        return '请输入用户名！'
if __name__ == '__main__':
    app.run(debug=True)
 ```
#### 2.  signals.py
```
#encoding:utf-8
from blinker import Namespace
from datetime import datetime

from flask import request,g

namespace = Namespace()

# 1.定义一个信号
login_signal = namespace.signal('login')
def login_log(sender):
    # 用户名，登陆时间，ip地址
    now = datetime.now()
    ip = request.remote_addr
    log_line = "{username}+{now}+{ip}".format(username=g.username,now=now,ip=ip)
    with open('login_log.txt','a') as fp:
        fp.write(log_line+"\n")
# 2.监听一个信号，将 login_log()函数写到 connect（）中
login_signal.connect(login_log)
```
