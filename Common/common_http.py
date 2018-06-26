import requests
from Common.common_Logger import *
import json

logger = myLog.getLog()



class Base_Requests(object):
    def __init__(self, method, host, params_url):
        self.host = host
        self.method = method
        self.params_url = params_url
        self.client = requests.Session()

    def sxs_Api(self, **kwargs):
        url = self.host + self.params_url
        logger.buildStartLine_info('请求地址为：%s' %url)

        #print(kwargs)
        if self.method == 'POST':
            kwargs = kwargs['data']['data']
            logger.buildStartLine_info('请求数据为：%s' % kwargs)
            #print(kwargs)
            r = self.client.post(url, data=kwargs)

            r.encoding = 'UTF-8'
            if r.status_code == 200:
                result = json.loads(r.text)
                logger.buildStartLine_info('请求结果为：%s' % result)
                return result
        else:
            r = self.client.get(url, params=kwargs)
            r.encoding = 'UTF-8'
            if r.status_code == 200:
                result = json.loads(r.text)
                logger.buildStartLine_info('请求结果为：%s' % result)
                return result