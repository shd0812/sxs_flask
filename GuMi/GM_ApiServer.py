from GuMi.gm_http import Base_Requests
import  json
from Common.common_Time import hh_Time
from GuMi.gumi_Tools import *
from Common.common_Logger import *
import ast
import traceback
from Common.common_Verify import eq_verify
logger = myLog.getLog()

def xx_post(url,host=0,special=0,**kwargs):
    method = 'POST'
    if host ==1:
        host = 'https://cyx.shaxiaoseng.com/Gumi/enc'
    elif host==0:
        host='https://mi.shaxiaoseng.com:4433/Gumi/dispatcher'
    elif host==2:
        host = 'https://cyx.shaxiaoseng.com/Gumi/dec'
    client = Base_Requests(method, host, url)

    result=client.sxs_Api(special,data=kwargs)
    return result

def send_post(parm_url,json_str):
    if not json_str:
         json_str = '{"index": {"name": "platformUserNo", "salt": "1234567891011111", "vals": ["6003115", "22222222"]}}'

    parm_dic={}
    body_dic={}
    try:
        user_dic = ast.literal_eval(json_str)

        parm_dic['service']=parm_url

        body_dic['body']=user_dic


        d3 = parm_dic.copy()
        d3.update(body_dic)

        result_parm_dic=json.dumps(d3)

        logger.debug('组装的参数字典为%s' %result_parm_dic)
        result = xx_post('',1, 1,data=result_parm_dic)
        result_data = xx_post('',  data=result)
        if json.loads(result_data).get('code')==500  :
            logger.debug('最终返回结果为:%s' % result_data)
            return result_data
        elif json.loads(result_data).get('code')==1999:
            logger.debug('最终返回结果为:%s' % result_data)
            return result_data
        else:
            result = xx_post('', 2, 1, data=result_data)
            logger.debug('最终返回结果为:%s' %result)
            return result
    except :
        traceback.print_exc()




if __name__ == '__main__':

    #send_post('queryUser','')
    path='../TestData/gm/invest.yaml'
    parm_dic=get_ParmData(path)
    url = parm_dic.get('service')
    parm_str=parm_dic.get('body')
    #print(url,parm_str)
    result = send_post(url,str(parm_str))
    eq_verify(json.loads(result),path)
    #print(result)