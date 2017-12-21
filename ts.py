#coding:utf-8
import requests
import json
import shd_code

# 底层 请求函数
def sxs_post(url_par,form_data):
	test_url ='https://ts.shaxiaoseng.com:4433/Api2/Api.php/'+url_par
	print test_url
	response = requests.post(test_url,data=form_data)
	t= response.content
	dic = eval(t)
	return dic
#获取 auth_id
def get_authid():
	form_data = {'app_name':'main','kid':'iOS_dfaed0881b9784bd5a2e2d036c44c00a','src':'IOS','version':'1.4.7'}
	url = 'Index'
	dic = sxs_post(url,form_data)
	dics = dic['data'][0]
	mid = dics['mid']
	
	auth = dics['auth']
	enauth= auth[6:14]
	deauth = auth[14:21]
	return mid,enauth,deauth
	
# 获取首页公告 
def get_index02():

	form_data = {'app_name':'main','auth_id':get_authid()[0],'src':'IOS','version':'1.4.7'}

	url = 'Index/index_02'
	dic = sxs_post(url,form_data)	
	return dic['Key']
#债权转让
def get_zhailist():
	url = 'Zhaizhuan/productList?'
	types ='all'
	types = shd_code.enc(types,get_authid()[1])
	page_num = '20'
	page_num = shd_code.enc(page_num,get_authid()[1])
	form_data = {'app_name':'main','auth_id':get_authid()[0],'src':'IOS','version':'1.4.7','type':types,'page_num':page_num}
	print form_data
	dic=sxs_post(url,form_data)
	print dic
	
	
def login():
	test_url = 'https://ts.shaxiaoseng.com:4433/Api2/Api.php/User/login/'
	phone = '18700113351'
	passwd = '123456'
	phone = shd_code.enc(phone,get_id()[1])
	print get_id()[1]
	passwd = shd_code.enc(passwd,get_id()[1])
	#print phone
	#print passwd
	#passwd = shd_code.enc(passwd,get_id()[1])
	form_data = {'app_name':'main','auth_id':get_authid()[0],'src':'IOS','version':'1.4.7','phone':phone,'userpwd':passwd}
	print form_data
	response = requests.post(test_url,data=form_data)
	t= response.content
	print response
	
	
	
	
	
if __name__ == '__main__':
 #解密
	sxs_dekey = get_authid()[2]
	#sss = get_index02()
	#sss=''
	sss='AyRndXpXXnJQYXF5VloHJ2d1f1VbBFVldX5WKwZUYwJ7UV5wVGd0DVZaB1dndX4nWgZQYXF9U1wCV2d1fyVddlEXdX5TWAJfY3N+Vlt1VGd0fldZB1BndX4nWgZRZXF1UlsDU2J1eidaBlUUdX5SUANSYnN7VF8HVRRyD1YuASVnAXtQXwdUEHB/UlACV2J/el1eBVATcH9SXQIjY3B+IV4HUBNxCFErBiBgcXpVXwFQFnB4USsGIGJye1Red1ATcX1SXAElZwF/VlsEVWR0e1dZB1Rmd39QWwVVYXR4V1AHU2Z1fiFedVFlcXtWWgYlZ3V7UV8GUBZ1flcpBlRjf3tQXwBRZXB/VykBJWcBeSdaclFhcH9WLQNVY396VV8MUGxxfVIuA1VjcnohXgNUEHF/Ui4CImYGf1BbAFVmdH9RKwYgY3Z6V18AUGxwelJRA1JifnknWnJQFnEKU14CU2ABelFfDVBgcH9RKwYgY356IV4AUGBwdFYtAl5ic3ogXndVE3F/UlACV2MCeiFeAVAWdAhQWQAnYQZ4U1wFUmF0ClNcAiBjBXpRXnFVEXF5U1EAJ2Z3elFdDFJkcXVQLgJfYQZ4Jl0CVWRyfVJRACVhdHglXgxQZ3N7UlsCX2EBel1cdVJscnlTKQBfZnZ4IV4NUmxwf1BRAiJid39UXgVTZnN1V14AX2MCeCFbAFBmcHVXWAdWYAZ6JVwCUBBzCFIpACNjf3ggXQBSFHF0UVEBVWEGf11acVBgcHVQKQNWY3R/V1xwUGxzClJRACdjAXpQXAxTZ3B7UC4CJWJwe1JdDFJmdHVXWwJSZnR6V18BUGZ0flJQAl5jcnhTXndQbXF+V1sAI2MEelZecFBmcHlRUQdUZn57UFwNUGxwe1JRAV9gf3lSXnZSbHENUi4CX2N2eFxdBlVlcX9QXANWY3R4J1sFUWJwelJcB1Vjc39XXHdQEHMJUi4BX2B/elxfBFNscntXUQMnYAZ5U1sBUBBzD1IsACNicXpWXQdSbHB/UFECImJ3f1ReBVNmc3VXXgBfYwJ4IVsAUGZwdVdYB1ZgBnolXAJQEHMIUikAI2N/eCBdAFIUcXRRUQFVYX57V1wNUBFxD1JQAlJhdHhdWwJSEXJ4UV0DXmEDeiVcDVVgcwlRXAFfYgZ4IF0HUWJxdVEpAV5jf3tTXA1QFHEKU1AAI2BzeFFbBFITc3hSXwdVYQJ6JVxwUW1zD1BbACdmdnpVXQNTZHF1UC4CX2F+e11ccFJhcnVTUAAjYgZ6V14NUGNyfVYtAF5ifn9TXgdRbXMKUVwAJGEFf1xeB1Jmcw9QKwNSYQZ5UV8DUGByeVJQACJjdntTXQJSZnR8V1ADXmF2eVxfAFFjcwpQKQJRYnB7U1wBVWVzfVBbACJndXsgXXBREQ=='
	
	print shd_code.dec(sss,sxs_dekey)
	#get_zhailist()
	
	
