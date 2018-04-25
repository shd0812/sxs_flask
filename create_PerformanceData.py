import shd_code
from sutils import sxs_db

#查询数据  96e79218965eb72c92a549dd5a330112 111111  e10adc3949ba59abbe56e057f20f883e 123456
def query_code():
	my_db = sxs_db('sxs_vault')
	#sql = "SELECT a.id,a.authkey,u.mobile,a.user_id FROM vault_user_auth a LEFT JOIN vault_user u on a.user_id = u.id WHERE u.login_pwd = 'e10adc3949ba59abbe56e057f20f883e'  GROUP BY u.mobile HAVING sum(u.mobile) >1 ORDER BY u.creat_time DESC"
	sql1="SELECT authkey,user_id,MAX(id) id FROM vault_user_auth WHERE inuse=1 AND user_id>300 GROUP BY user_id ORDER BY id DESC  LIMIT 2000"
	data = my_db.get_data(sql1)
	print(data[0])
	return data

#加密后，组成压测数据
def encry_parm():
	result_list = [] 
	list_data = query_code()
	for list in list_data:
		#mobile = list['mobile']
		#passwd='123456'
		mid= str(list['id'])
		uid=str(list['user_id'])
		authkey= list['authkey']
		enauth= authkey[6:14]
		#form_data ='phone=%s&userpwd=%s' % (mobile,passwd)
		form_data='user_id=%s' % uid
		form_data =  shd_code.encryt_sxs(form_data,enauth)
		#print(form_data)
		if '+' in form_data:
			print('222')
		else:
			results=mid+','+form_data
			result_list.append(results)
	#print(result_list)
	return result_list


	
def writeFile():
	list = encry_parm()
	#list = ['4','5','6']
	with open('d:/test5_data', 'a') as f:
		for l in list:
			f.writelines('%s\n' % l)
		

	
if __name__=='__main__':
	#encry_parm()
	writeFile()