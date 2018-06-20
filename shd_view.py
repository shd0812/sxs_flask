#coding:utf-8
from flask import Flask
from flask import request,flash
from flask import render_template
from sutils import sxs_db
from sxs_loan import get_loanID
from Transfer.transfer_server import switch_tran
from flask import Blueprint,jsonify

admin = Blueprint('admin', __name__)


#app = Flask(__name__)

@admin.route('/', methods=['GET', 'POST'])
def home():
	datas = [
	{'url':'/admin/user',
	'btn_name':'查询用户信息'},
	{'url':'/admin/create',
	'btn_name':'贷款端建标'},
	{'url':'/admin/repay',
	'btn_name':'还款以及债转'},
		{'url': '/home/',
		 'btn_name': '星火项目'}
	]
	return render_template('index.html',datas=datas)
#查询用户信息
@admin.route('/user', methods=['POST'])
def user():
	return render_template('user.html')
#用户验证码	
@admin.route('/user_code', methods=['POST'])
def user_code():
	my_db = sxs_db('sxs_vault')
	mobile = request.form['mobile']
	if mobile =='':
		flash('2222222222')
	else:
		sql = "SELECT verify FROM vault_user_mobile_verify WHERE mobile = '%s' ORDER BY ID DESC LIMIT 1 " % mobile 
		data = my_db.get_data(sql)
		print (data)
		sex = data[0]['verify']
		flash('您的验证码为%s' % sex)
	return render_template('user.html')

	#用户信息
@admin.route('/user_detail', methods=['POST'])
def user_detail():
	my_db = sxs_db('sxs_vault')
	mobile = request.form['mobile']	
	sql = "SELECT id,real_name ,platform_user_no,mobile,invite_id,friend_id,channel_type FROM vault_user WHERE mobile = '%s'" % mobile 
	data = my_db.get_data(sql)
	key=(data[0]['id'])
	print(type(key))
	return render_template('user_detail.html',datas=data)

#用户投资情况

@admin.route('/user_tender', methods=['POST'])
def user_tender():
	my_db = sxs_db('sxs_vault')
	mobile = request.form['mobile']
	if len(mobile)==14:
		sql = "SELECT real_name,user_id,platform_user_no,mobile,project_no,deal_no,in_money,in_time,`status`,biz_status,request_no,redpack_money,type,loan_time,subscription_time,remaining_amount,remaining_available_transfer_amount FROM vault_user_invest_trade_log WHERE project_no = '%s' " % mobile
		
	elif len(mobile)==11:
		sql = "SELECT real_name,user_id,platform_user_no,mobile,project_no,deal_no,in_money,in_time,`status`,biz_status,request_no,redpack_money,type,loan_time,subscription_time,remaining_amount,remaining_available_transfer_amount FROM vault_user_invest_trade_log WHERE mobile = '%s'" % mobile
	else:
		sql = "SELECT real_name,user_id,platform_user_no,mobile,project_no,deal_no,in_money,in_time,`status`,biz_status,request_no,redpack_money,type,loan_time,subscription_time,remaining_amount,remaining_available_transfer_amount FROM vault_user_invest_trade_log WHERE user_id = '%s' " % mobile
	data = my_db.get_data(sql)
	
	
	my_db = sxs_db('sxs_vault')
	mobile = request.form['mobile']
	if len(mobile)==14:
		sql= "SELECT user_id,project_no,date,term_no,principal,interest,add_interest,state,request_no,last_time,repay_time,is_ahead_repay FROM vault_user_repayment_log WHERE project_no = '%s'" % mobile
		
	elif len(mobile)==11:
		sql= "SELECT user_id,project_no,date,term_no,principal,interest,add_interest,state,request_no,last_time,repay_time,is_ahead_repay FROM vault_user_repayment_log WHERE user_id = (SELECT id FROM vault_user WHERE mobile='%s')" % mobile
	else:
		sql= "SELECT user_id,project_no,date,term_no,principal,interest,add_interest,state,request_no,last_time,repay_time,is_ahead_repay FROM vault_user_repayment_log WHERE user_id = '%s'" % mobile
	repay_data = my_db.get_data(sql)
	
	#repay_datas=my_db.get_data(sql1)
	return render_template('user_tender.html',datas=data,repay_datas=repay_data)

	
	
#创建标的
@admin.route('/create', methods=['POST'])
def create():
	return render_template('creatloan.html')

def loan(loan_type,idcard,times,title,money,month,yearRates,dailyRate):
	start_num =1
	times = int(times)
	while (start_num < times):
		data=get_loanID(loan_type,title,idcard,money,month,yearRates,dailyRate)
		start_num+=1
	return data
@admin.route('/create_loan', methods=['POST'])
def create_loan():
	loan_type = request.form['loantype']
	idcard = request.form['idcard']
	num = request.form['num']
	title = request.form['title']
	money = request.form['money']
	yearRates = request.form['yearRates']
	month=request.form['month']
	dailyRate=request.form['dailyRate']
	if dailyRate=='':
		print('日利率%s' % dailyRate)
	else:
		yearRates = float('%.2f' % (float(dailyRate)*360))
	print(yearRates,dailyRate)
	msg_code=loan(loan_type,idcard,num,title,money,month,yearRates,dailyRate)

	#flash(msg_code)
	print(msg_code)
	return jsonify(msg_code)
	
#还款以及债转
@admin.route('/repay',methods=['POST'])
def repay():
	return render_template('repay.html')
@admin.route('/up_repay',methods=['POST'])
def up_repay():
	begin_type = request.form['begin_end']

	invest_id = request.form['invest_id']

	if invest_id=='':
		ss='输入不能为空'
	else:
		ss=switch_tran(begin_type,invest_id)
	return jsonify(ss)



	

# if __name__ == '__main__':
	
	# app.run(host='0.0.0.0',port=5001,debug=True)
	