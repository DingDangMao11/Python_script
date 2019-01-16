#### 1、
```
from flask import Flask,url_for,render_template
from flask_restful import Api,Resource


app = Flask(__name__)
api = Api(app)

class LoginView(Resource):
    def post(self):
        return {"username"}
# 使用url_for反转时，可以使用endpoint
api.add_resource(LoginView,'/login/',endpoint='login')
@app.route('/')
def index():
    return "hello  world"

if __name__ == '__main__':
    app.run()
```

#### 2、
```
from flask import Flask,url_for,render_template
from flask_restful import Api,Resource


app = Flask(__name__)
api = Api(app)

class LoginView(Resource):
    def post(self):
        return {"username":"zhiliao"}
# 使用url_for反转时，可以使用endpoint
api.add_resource(LoginView,'/login/',endpoint='login')

@app.route('/')
def index():
    return "hello world"

if __name__ == '__main__':
    app.run()

    
```
#### 3、
```
from flask import Flask,url_for,render_template
from flask_restful import Api,Resource


app = Flask(__name__)
api = Api(app)

class LoginView(Resource):
    def post(self):
        return {"username":"zhiliao"}
# 使用url_for反转时，可以使用endpoint
api.add_resource(LoginView,'/login/')
with app.test_request_context():
    print(url_for('loginview'))
@app.route('/')
def index():
    return "hello world"

if __name__ == '__main__':
    app.run()

    
```
#### 4、
```
from flask import Flask,url_for,render_template
from flask_restful import Api,Resource


app = Flask(__name__)
api = Api(app)

class LoginView(Resource):
    def post(self,username):
        return {"username":"zhiliao"}
# 使用url_for反转时，可以使用endpoint
api.add_resource(LoginView,'/login/<username>')
with app.test_request_context():
    #print(url_for('loginview'))
    print(url_for('loginview',username='zhilaio')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
```
#### 5、
```
from flask import Flask,url_for,render_template
from flask_restful import Api,Resource


app = Flask(__name__)
api = Api(app)

class LoginView(Resource):
    def post(self,username=None):
        return {"username":"zhiliao"}
api.add_resource(LoginView,'/login/<username>','/regist/')
with app.test_request_context():
     print(url_for('loginview',username='zhilaio'))


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    
http://127.0.0.1:5000/regist/
```
# 参数验证
```
#encoding:utf-8
from flask import Flask,url_for,render_template
from flask_restful import Api,Resource,reqparse


app = Flask(__name__)
api = Api(app)

class LoginView(Resource):
    def post(self):
        # username
        # password
        parser = reqparse.RequestParser()
        # 1.默认username为abc，不用再输入username
        # parser.add_argument('username',type = str,help='用户名验证错误',default='abc')
        # 2.required指定为True，username必须传递。如果不传递required，默认为false
        # parser.add_argument('username',type = str,help='用户名验证错误',required=True)
        # 3.trim去掉输入字符串中的空格
        #parser.add_argument('username', type=str, help='用户名验证错误',trim=True)
        # 3.telphone符合正则表达式规范
        # parser.add_argument('telphone', type=inputs.regex(r'1[3578]\d{9}'))
        # 4.birthday必须为时间
        # parser.add_argument('birthday', type=inputs.date,help='生日字段验证错误！')
        parser.add_argument('password',type=str,help='密码验证错误')
        parser.add_argument('sex', type=str, choices=['male','female','secret'])
        # 解析数据
        args = parser.parse_args()
        print(args)
        return {"username":"zhiliao"}

api.add_resource(LoginView,'/login/')
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

```
```
#encoding:utf-8
from flask import Flask,url_for,render_template
from flask_restful import Api,Resource,reqparse


app = Flask(__name__)
api = Api(app)

class LoginView(Resource):
    def post(self):
        # username
        # password
        parser = reqparse.RequestParser()
        # 1.默认username为abc，不用再输入username
        # parser.add_argument('username',type = str,help='用户名验证错误',default='abc')
        # 2.required指定为True，username必须传递。如果不传递required，默认为false
        # parser.add_argument('username',type = str,help='用户名验证错误',required=True)
        # 3.trim去掉输入字符串中的空格
        #parser.add_argument('username', type=str, help='用户名验证错误',trim=True)
        # 3.telphone符合正则表达式规范
        # parser.add_argument('telphone', type=inputs.regex(r'1[3578]\d{9}'))
        # 4.birthday必须为时间
        # parser.add_argument('birthday', type=inputs.date,help='生日字段验证错误！')
        parser.add_argument('password',type=str,help='密码验证错误')
        parser.add_argument('sex', type=str, choices=['male','female','secret'])
        # 解析数据
        args = parser.parse_args()
        print(args)
        return {"username":"zhiliao"}

api.add_resource(LoginView,'/login/')
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

```
