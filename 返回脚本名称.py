from flask import Flask, current_app
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

with app.app_context():
    print(current_app.name)

@app.route('/')
def index():
    print(current_app.name)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
