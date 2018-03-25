#coding:utf-8
from flask import Flask
from flask_script import Manager
app = Flask(__name__)
app.secret_key = '123'
#manager = Manager(app)

from shd_view import admin
app.register_blueprint(admin,url_prefix='/admin')

from login import login
app.register_blueprint(login,url_prefix='/login')

if __name__ == '__main__':
	#manager.run()
	app.run(host='0.0.0.0',port=5000,debug=True)