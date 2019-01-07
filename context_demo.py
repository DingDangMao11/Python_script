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
