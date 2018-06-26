from Common.common_http import Base_Requests
import  json
from Common.common_Time import hh_Time
from GuMi.gumi_Tools import *


def xx_post(url,**kwargs):
    method = 'POST'
    host = 'https://mm.shaxiaoseng.com/Gumi/dispatcher/'
    client = Base_Requests(method, host, url)

    result=client.sxs_Api(data=kwargs)
    return result

def send_post(parm_url,json_str):
    hh = hh_Time()
    ase = ase_GuMi()
    parm_dic={}
    if not json_str:
        json_str = '{"Index": {"name": "11111111", "salt": "asdfgkjb", "vals": ["11111111", "22222222"]}}'

    data= ase.encrypt(json_str)

    timestamp=str(hh.getTimestamp())
    nonce=''
    signature=create_Sign(data)
    parm_dic['data']=data
    parm_dic['timestamp'] = timestamp
    parm_dic['nonce'] = nonce
    parm_dic['signature'] = signature
    logger.buildStartLine_info('组装的参数字典为%s' %parm_dic)
    if parm_dic =='输入参数不合法':
        return parm_dic
    else:
        #print(111)
        result=xx_post(parm_url,data=parm_dic)
        return result


if __name__ == '__main__':
    print('2222')
    send_post('111','')