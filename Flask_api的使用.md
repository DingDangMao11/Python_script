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
with app.test_request_context():
    print(url_for('loginview'))

@app.route('/')
def index():
    return "hello  world"

if __name__ == '__main__':
    app.run()
```
```
from flask import Flask,url_for,render_template
from flask_restful import Api,Resource


app = Flask(__name__)
api = Api(app)

class LoginView(Resource):
    def post(self,username):
        return {"username":"zhiliao"}
# 使用url_for反转时，可以使用endpoint
api.add_resource(LoginView,'/login/')
with app.test_request_context():
    #print(url_for('loginview'))
    print(url_for('loginview',username='zhilaio'))


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    
```
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
