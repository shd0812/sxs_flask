#coding:utf-8
from flask import Flask
from flask import request,flash
from flask import render_template
from sutils import sxs_db
from sxs_loan import get_loanID

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
	my_db = sxs_db('sxs_vault')
	mobile = request.form['mobile']
	# mobile = '13801000001'
	sql = "SELECT verify FROM vault_user_mobile_verify WHERE mobile = '%s' ORDER BY ID DESC LIMIT 1 " % mobile 
	data = my_db.get_data(sql)
	print (data)
	sex = data[0]['verify']
	flash('您的验证码为%s' % sex)
	return render_template('test1.html')

@admin.route('/create', methods=['POST'])
def create():
	return render_template('creatloan.html')

def loan(loan_type,idcard,times,title):
	start_num =1
	times = int(times)
	while (start_num < times):
		get_loanID(loan_type,title,idcard)
		start_num+=1
	
@admin.route('/create_loan', methods=['POST'])
def create_loan():
	loan_type = request.form['loantype']
	idcard = request.form['idcard']
	num = request.form['num']
	title = request.form['title']
	loan(loan_type,idcard,num,title)
	return '已成功'	
# if __name__ == '__main__':
	
	# app.run(host='0.0.0.0',port=5001,debug=True)
	