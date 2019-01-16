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
