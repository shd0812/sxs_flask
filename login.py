from flask import Flask,request,render_template,Blueprint,flash
from sutils import sxs_db


login = Blueprint('login', __name__)
#login.secret_key = '123' 



@login.route('/', methods=['GET', 'POST'])
def home():
	return render_template('login.html')

@login.route('/next', methods=['GET', 'POST'])
def next():
	my_db = sxs_db('dd_test')
	phone = request.form['phone']
	passwd = request.form['passwd']
	sql = "SELECT passwd FROM tester WHERE account = '%s'" % phone
	data = my_db.get_data(sql)
	passwd1 = data[0]['passwd']
	print (passwd,passwd1)
	if passwd == passwd1:
		return '222'
	else:
		flash('密码输入错误,请重新输入')
		return render_template('login.html')
		