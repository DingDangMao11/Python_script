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
#  捕获错误调用相应的钩子函数
@app.errorhandler(500)
def server_error(error):
    # return '服务器刷新的太频繁'
    return render_template('500.html'),500
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
500.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h2>服务器刷新的太频繁</h2>
</body>
</html>
404.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h2>搜索的页面到火星了</h2>
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
