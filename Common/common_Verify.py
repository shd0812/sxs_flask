from common_OpFile import operate_File
from common_Logger import *
logger = myLog.getLog()


def eq_verify(check_data,path):
    if not path:
        path='../TestData/gm/valid.yaml'
    op =operate_File(path)
    d=op.read_file()
    expect_list=d.get('expect')
    #print(expect_list)
    for item in expect_list:
        logger.debug('期待的hahahahahhaha{}'.format(item))
        key,=item

        temp_li=key.split('.')
        logger.debug('期待的keykeykeykey----{}'.format(temp_li))
        logger.debug('传输过来的----{}'.format(check_data))
        tmp= check_data
        for x in range(len(temp_li)):
            result_data = temp_li[x]
            if isinstance(tmp,dict):

                tmp=tmp.get(result_data)

            elif isinstance(tmp,list):
                tmp=tmp[int(result_data)]




        check_str=tmp
        expect_str = item.get(key)
        logger.info('要检查的字符{},期待的字符{}'.format(check_str,expect_str))

        if check_str == expect_str:
            pass
        else:
            raise Exception('不相等，要检查的是{},期望的是{}'.format(check_str,expect_str))


if __name__ == '__main__':
    check_data={
            'test_name':'用户信息查询',
            'parm':{
                'service':'bind_url',
                'body':[{
                    'index':{
                        'name':'shen',
                        'vals':[111111,222222],
                        'sex' : 5
                    }
                    }]
                }

            }

    #eq_verify(check_data,'')
   # print('服务器返回{}'.format(check_data))
    check_list=['parm.body.0.index.name','parm.body.0.index.sex']
    #print(check_data)

    for item in  range(len(check_list)):
        s_item = check_list[item]
        ss = s_item.split('.')
        tmp = check_data
       # print("=========11111===%s"%ss)

        for x in range(len(ss)):
            result_data = ss[x]
            if isinstance(tmp,dict):

                tmp=tmp.get(result_data)
                print('xx:{}'.format(tmp))
            elif isinstance(tmp,list):
                tmp=tmp[int(result_data)]
                print('yy: {}'.format(tmp))




    #print(check_list)
