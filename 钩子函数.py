from flask import Flask,session,g
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    # 判断g是否有user这个属性
    if hasattr(g,'user'):
        print(g.user)
    return 'hello world'


@app.route('/list/')
def my_list():
    session['user_id'] = 1
    return 'my list'
# 钩子函数只有在第一次时才会执行
# @app.before_first_request
# def first_request():
#     print('hello_world')


@app.before_request
def before_request():
    #print('在视图函数之前执行的钩子函数')
    user_id = session.get('user_id')
    if user_id:
        g.user = 'zhiliao'
if __name__ == '__main__':
    app.run()
utils.html
#encoding:utf-8
from flask import g
def log_a():
    print('log a %s' % g.username)

def log_b():
    print('log b %s' % g.username)

def log_c():
    print('log c %s' % g.username)
-------------------------------------------------------------------------
from flask import Flask,session,g,render_template
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    # 判断g是否有user这个属性
    if hasattr(g,'user'):
        print(g.user)
    return render_template('index.html')


@app.route('/list/')
def my_list():
    session['user_id'] = 1
    return render_template('list.html')


@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        g.user = 'zhiliao'

# 在所有的页面中显示current_user的值
@app.context_processor
def context_processor():
    # return  {"current_user":'zhiliao'}
    if hasattr(g, 'user'):
        return {"current_user": g.user}
    else:
        return {}
if __name__ == '__main__':
    app.run()

index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    {{ current_user }}
</body>
</html>

list.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    {{ current_user }}
</body>
</html>
-------------------------------------------------------------------------------------
### 常用的钩子函数：
在Flask中钩子函数是使用特定的装饰器装饰的函数。为什么叫做钩子函数呢，是因为钩子函数可以在正常执行的代码中，插入一段自己想要执行的代码。那么这种函数就叫做钩子函数。（hook）
1. `before_first_request`：Flask项目第一次部署后会执行的钩子函数。
2. `before_request`：请求已经到达了Flask，但是还没有进入到具体的视图函数之前调用。一般这个就是在视图函数之前，我们可以把一些后面需要用到的数据先处理好，方便视图函数使用。
3. `context_processor`：使用这个钩子函数，必须返回一个字典。这个字典中的值在所有模版中都可以使用。这个钩子函数的函数是，如果一些在很多模版中都要用到的变量，那么就可以使用这个钩子函数来返回，而不用在每个视图函数中的`render_template`中去写，这样可以让代码更加简洁和好维护。
4. `errorhandler`：在发生一些异常的时候，比如404错误，比如500错误。那么如果想要优雅的处理这些错误，就可以使用`errorhandler`来出来。需要注意几点：
    * 在errorhandler装饰的钩子函数下，记得要返回相应的状态码。
    * 在errorhandler装饰的钩子函数中，必须要写一个参数，来接收错误的信息，如果没有参数，就会直接报错。
    * 使用`flask.abort`可以手动的抛出相应的错误，比如开发者在发现参数不正确的时候可以自己手动的抛出一个400错误。
示例代码如下：
```python
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404
```
