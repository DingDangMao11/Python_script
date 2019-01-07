from flask import Flask, current_app, url_for
from werkzeug.local import Local

# 只要绑定在Local对象上的属性
# 在每个线程中都是隔离的



app = Flask(__name__)

# 栈
#方法1
# app_context = app.app_context()
# app_context.push()
# print(current_app.name)
#方法2

# with app.app_context():
#     print(current_app.name)

@app.route('/')
def index():
    # print(current_app.name)
    print(url_for('my_list'))
    return 'Hello World!'
@app.route('/list/')
def my_list():
    return 'my list'

with app.test_request_context():
    # 手动推入一个请求上下文到请求上下文栈中
    # 如果当前应用上下文栈中没有应用上下文
    # 那么会首先推入一个应用上下文到栈中
    print(url_for("my_list"))
if __name__ == '__main__':
    app.run()
    
----------------------------------------------------------------------------------------
app.py
from flask import Flask, current_app, url_for,g,request,session
from werkzeug.local import Local
from utils import log_a,log_b,log_c

app = Flask(__name__)

@app.route('/')
def index():
    print(url_for('my_list'))
    username = request.args.get('username')
    log_a(username)
    log_b(username)
    log_c(username)

    return 'Hello World!'
@app.route('/list/')
def my_list():
    return 'my list'

with app.test_request_context():
    # 手动推入一个请求上下文到请求上下文栈中
    # 如果当前应用上下文栈中没有应用上下文
    # 那么会首先推入一个应用上下文到栈中
    print(url_for("my_list"))
if __name__ == '__main__':
    app.run()
    
utils.py
#encoding:utf-8

def log_a(username):
    print('log a %s' % username)

def log_b(username):
    print('log b %s' % username)

def log_c(username):
    print('log c %s' % username)
    
网址输入：http://127.0.0.1:5000/?username=zhiliao
