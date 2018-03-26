#coding:utf-8
import time
import pymysql

	
#操作文件类	
class handlefile():
	def __init__(self,path):
		self.path = path
	#读取文件
	def read_file(self,filename):
		with open(self.path+filename,'rb') as pf:
			sxs_list = []
			data = pf.readlines()
			for i in data:
				list = i.split(',')
				#print list
				sxs_list.append(list)
			return sxs_list
	#写入文件
	def write_file(self,filename,strs):
		with open(self.path+filename,'a') as pf:
			pf.write(strs+'\n')

class shd_time():
	
	#获取当前时间戳
	def getTimestamp(self):
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
	
	#指定时间转成为时间戳
	def time_tran(self,s_time):
		#转换成时间数组
		timeArray = time.strptime(s_time, "%Y-%m-%d %H:%M:%S")
		#转换成时间戳
		timestamp = time.mktime(timeArray)
		return int(timestamp)		
	#时间戳转换成时间
	def tamp_tran(self,s_tamp):
		#转换成localtime
		time_local = time.localtime(s_tamp)
		#转换成新的时间格式(2016-05-05 20:28:54)
		dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
		return dt		

	
#操作数据库
# 参数化sql 有 两种方式，一种是字典，另一种是 目前正在用的
	# sql = '''
	   # UPDATE vault_user_mobile_verify SET verify = '56' WHERE mobile = %(phone)s
	   # '''
	   
	# vaule = {"phone":'18700112233'}
	# cursor.execute(sql,vaule)
class sxs_db():
	def __init__(self,db_name):
		try:
			self.db = pymysql.connect(host='192.168.130.203',port=9309\
			,user='root',passwd='sxslocalhost2017'\
			,db=db_name,use_unicode=True,charset='utf8')
		except Exception as e:
			print('mysql 连接失败')
		else:
			self.cursor=self.db.cursor(cursor=pymysql.cursors.DictCursor)#转化为字典
			
	def get_data(self,sql,*k):
			try:
				self.cursor.execute(sql,k)
			except Exception as e:
				print('sql执行失败')
				return 'sql_error',e
			else:
				self.db.commit()
				return self.cursor.fetchall()

				
if __name__ == '__main__':
	my_db = sxs_db('sxs_vault')
	mobile = '13801000001'
	sql = "SELECT verify FROM vault_user_mobile_verify WHERE mobile = '%s'" % mobile
	print (my_db.get_data(sql))
	
	#hand = handlefile('d:/')
	#hand.read_file('11.txt')
	#hand.write_file('22.txt','2')
	#print hand.read_file('name.txt')[0][0]
	#print getTimestamp()
	
	#dt = "2016-05-05 20:28:54"
	
	#timestamp = 1462451334
	
	
	sxs_time = shd_time()
	str1 = str(sxs_time.getTimestamp())
	lenth = len(str1)
	print (str1,str1[lenth-3:lenth])
	#print sxs_time.time_tran(dt)
	#print sxs_time.tamp_tran(timestamp)
	
	
	
	
	
	