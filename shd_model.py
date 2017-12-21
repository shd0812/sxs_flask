#coding:utf-8
import sys
sys.path.append('D:\Python\shd_tools')
import tools

def get_auth(mobile):
	sxs_hehe = tools.sxs_db('sxs_vault')
	#mobile='13801000010'
	authkey=sxs_hehe.get_data("SELECT authkey FROM vault_user_auth as a LEFT JOIN vault_user as u on a.user_id = u.id WHERE    inuse=1 AND mobile = '%s'" % mobile)
	
	auth_id = authkey[0]['authkey'][14:21]
	print auth_id
	return auth_id

if __name__=='__main__':
	get_auth('13801000020')
#print get_auth('13801000010')