# coding:utf-8
import requests
import json
import time
from bs4 import BeautifulSoup
import sxs_db 

#获取当前时间戳
def getTimestamp():
	#获取当前时间
	time_now = int(time.time())
	#转换成localtime
	time_local = time.localtime(time_now)
	#转换成新的时间格式(2016-05-09 18:59:20)
	dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
	timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
	timestamp = time.mktime(timeArray)
	return int(timestamp)

def getSigns(orderid):
#headers = {'Content-Tpye':'application/json','sign':"4505ab90c7eeb2e8d20d2ef2cb3bb982cdd8c656"}
	test_url = 'https://ts.shaxiaoseng.com:4433/public/index.php/api/getSign?'
	form_data = {'appkey':'20170002','nonce':'23234423','order_amount':399,'order_id':orderid,'order_status':'LOCKED',
	'order_time':'2017-10-19 16:31:36','receiver_city':'Shenzhen','receiver_mobile':'13802254331','receiver_name':'Leo','receiver_phone':'075523131','timestamp':getTimestamp()}
	response = requests.post(test_url,data=form_data)
	t= response.text.encode('GBK','ignore')

	soup = BeautifulSoup(t,'html.parser')
	sl = soup.find_all("span")
	sign = [span.get_text() for span in sl]
	sign = ','.join(sign)
	#print orderid
	return sign
#生成订单主方法	
def create_order(orderid):
	test_url2 = 'https://ts.shaxiaoseng.com:4433/public/index.php/api/peixingzhe/store'
	form_data = {'appkey':'20170002','nonce':'23234423','order_amount':399,'order_id':orderid,'order_status':'LOCKED',
	'order_time':'2017-10-19 16:31:36','receiver_city':'Shenzhen','receiver_mobile':'13802254331','receiver_name':'Leo','receiver_phone':'075523131','timestamp':getTimestamp()}
	headers = {'Content-Tpye':'application/json','sign':getSigns(orderid)}
	responses = requests.post(test_url2,data=form_data,headers=headers)
	tt= responses.text.encode('GBK','ignore')
	print tt
	
	
#批量生成订单号
def batch_create(order,num):
	#orderid = 777781
	#orderid = 777785
	#count 为 批量生成几个
	order= int(order)
	num = int(num)
	end_num = order+num
	#print end_num
	while (order < end_num):
		print '33'
		order = order +1
		create_order(order)
	return 'success'
# 订单插询
def select_order(orderid):
	url = 'https://ts.shaxiaoseng.com:4433/public/index.php/api/peixingzhe/index'
	par_data ='?order_id='+str(orderid)
	
	sxs_url= url+par_data
	print sxs_url
	response = requests.get(sxs_url)
	#response = requests.post(test_url,data=form_data)
	t= response.text
	print t
	return t
	
#订单失效	
def destroy_order(orderid):
	url = 'https://ts.shaxiaoseng.com:4433/public/index.php/api/peixingzhe/destroy'
	par_data ='?order_id='+str(orderid)
	
	sxs_url= url+par_data
	print sxs_url
	response = requests.get(sxs_url)
	#response = requests.post(test_url,data=form_data)
	t= response.text
	print t
	return t
# 失效后，查询数据库状态是否是2
def query_state(order):
	#status` '订单状态 1:生效 2：失效
	db = sxs_db.sxs_connectdb()
	sql = "SELECT status FROM vault_order_peixingzhe WHERE order_id ='%s'" % order
	data = db.get_data(sql)
	print data 
	status=int(data[0]['status'])
	code=''
	if status ==1:
		code= u'订单生效中'
		print code
	else:
		code=u'订单已失效'
		print code
	
	
if __name__ =='__main__':
	
	#批量生成订单号 
	#batch_create(888000,3)
	
	#destroy_order(orderid)
	#查询数据库订单状态
	query_state(777781)
	#select_order(orderid)




