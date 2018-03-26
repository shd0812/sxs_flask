# coding:utf-8
import time
import pymysql
from yaml import  load
from configparser import ConfigParser
import os

# 操作文件类
class operate_file():
	def __init__(self, file_name):
		self.file_name = file_name
		#print(file_name)

	def open(self):
		config_path = os.path.join(os.path.dirname(__file__), self.file_name)
		print(config_path)
		type = self.file_name.split('.')[1]
		if type == 'yaml':
			with open(config_path,'rb') as pf:
				data = load(pf)
			return	data
		elif type == 'ini':
			dd_config = ConfigParser()
			dd_config.read(config_path)
			return	dd_config





class shd_time():
	# 获取当前时间戳
	def getTimestamp(self):
		# 获取当前时间
		time_now = int(time.time())
		# 转换成localtime
		time_local = time.localtime(time_now)
		# 转换成新的时间格式(2016-05-09 18:59:20)
		dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
		timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
		# 转换成时间戳
		timestamp = time.mktime(timeArray)
		return int(timestamp)

	# 指定时间转成为时间戳
	def time_tran(self, s_time):
		# 转换成时间数组
		timeArray = time.strptime(s_time, "%Y-%m-%d %H:%M:%S")
		# 转换成时间戳
		timestamp = time.mktime(timeArray)
		return int(timestamp)

	# 时间戳转换成时间
	def tamp_tran(self, s_tamp):
		# 转换成localtime
		time_local = time.localtime(s_tamp)
		# 转换成新的时间格式(2016-05-05 20:28:54)
		dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
		return dt


		# 操作数据库
		# 参数化sql 有 两种方式，一种是字典，另一种是 目前正在用的
		# sql = '''
		# UPDATE vault_user_mobile_verify SET verify = '56' WHERE mobile = %(phone)s
		# '''

		# vaule = {"phone":'18700112233'}
		# cursor.execute(sql,vaule)


class sxs_db():
	operate_file = operate_file('config.ini')
	data=operate_file.open()
	global host,port,user,passwd
	host = data['mysql_config']['host']
	port = int(data['mysql_config']['port'])
	user = data['mysql_config']['account']
	passwd = data['mysql_config']['passwd']
	#print(host,type(port),user,passwd)
	def __init__(self, db_name):
		
		try:
			print(111)
			
			self.db = pymysql.connect(host=host, port=port \
									  , user=user, passwd=passwd\
									  , db=db_name, use_unicode=True, charset='utf8')
		except Exception as e:
			print(port)
			print('mysql 连接失败')
		else:
			self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)	 # 转化为字典

	def get_data(self, sql, *k):
		try:
			self.cursor.execute(sql, k)
		except Exception as e:
			print('sql执行失败')
			return 'sql_error', e
		else:
			self.db.commit()
			return self.cursor.fetchall()


def ob_element(data,num):
	return data['test_element'][num]['test_control']
		
def ob_valite(data):
	return data['test_valite']

			
if __name__ == '__main__':
	my_db = sxs_db('sxs_vault')
	mobile = '13801000001'
	sql = "SELECT real_name from vault_user WHERE mobile = '%s'" % mobile  
	print(my_db.get_data(sql))
	
	#print(ob_element(data,1))
	#print(data['test_element'][0]['test_control'],data)
	



	# sxs_time = shd_time()
	# str1 = str(sxs_time.getTimestamp())
	# lenth = len(str1)
	# print(str1, str1[lenth - 3:lenth])
# print sxs_time.time_tran(dt)
# print sxs_time.tamp_tran(timestamp)





