import requests

class base_request(object):
	def __init__(self,url):
		self.url = url
		
	@staticmethod
	def get_cookie(self,form_data):
		r=requests.post(self.url,form_data)
		_cookies=r.cookies
		return _cookies

	def to_post(self,url,form_data):
		r=requests.post(url,form_data,cookies=self.get_cookie())
		res_data=r.json()
		return res_data