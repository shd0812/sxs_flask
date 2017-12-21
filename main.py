#coding:utf-8
from flask import Flask

app = Flask(__name__)

from shd_view import admin
app.register_blueprint(admin,url_prefix='/admin')

if __name__ == '__main__':
	
	app.run(host='0.0.0.0',port=5000,debug=True)