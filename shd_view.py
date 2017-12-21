#coding:utf-8
from flask import Flask
from flask import request
from flask import render_template
import ts
import shd_code
import shd_model
import peixingzhe.orderid
from flask import Blueprint

admin = Blueprint('admin', __name__)


#app = Flask(__name__)

@admin.route('/', methods=['GET', 'POST'])
def home():
	return render_template('hello.html')

@admin.route('/signin', methods=['POST'])
def signin():
	
	return render_template('test1.html')
	
@admin.route('/page_one', methods=['POST'])
def page_one():
	sss = request.form['shd_str']
	mobile = request.form['mobile']
	return shd_code.dec(sss,shd_model.get_auth(mobile))

@admin.route('/act', methods=['POST'])
def act():
	return '''<form action="/admin/order_id" method="post">
			  <p>请输入起始订单号和生成的数量</p>
			  <p><input name="order" size="40"></p>
			  <p><input name="num" size="40"></p>
			  <p><button type="submit">生成</button></p>
			  </form>'''
@admin.route('/order_id', methods=['POST'])
def order_id():
	od = request.form['order']
	num =request.form['num']
	return peixingzhe.orderid.batch_create(od,num)
	
# if __name__ == '__main__':
	
	# app.run(host='0.0.0.0',port=5001,debug=True)
	