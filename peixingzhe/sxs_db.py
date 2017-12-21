#coding:utf-8
import pymysql


class sxs_connectdb():
	def __init__(self):
		try:
			self.db = pymysql.connect(host='192.168.130.203',port=9309\
			,user='root',passwd='sxslocalhost2017'\
			,db='sxs_vault',use_unicode=True,charset='utf8')
		except Exception as e:
			print('mysql 连接失败')
		else:
			self.cursor=self.db.cursor(cursor=pymysql.cursors.DictCursor)#转化为字典
			
	def get_data(self,sql):
			try:
				self.cursor.execute(sql)
			except Exception as e:
				print('sql执行失败')
				return 'sql_error',e
			else:
				self.db.commit()
				return self.cursor.fetchall()
	

	
	
if __name__ == '__main__':
	
	db = sxs_connectdb()
	order_id = 777781
	print type(order_id)
	sql = "SELECT status FROM vault_order_peixingzhe WHERE order_id ='%s'" % order_id
	print sql
	data = db.get_data(sql)
	print data[0]['status']
	#sxs_query(777781)