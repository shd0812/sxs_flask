import os
from yaml import  load
from configparser import ConfigParser
import json
# 操作文件类
class operate_File():

    def __init__(self,file_name):
        self.file_name=file_name
    #获取路径
    def get_path(self):
        path=os.path.dirname( __file__)
        parent_path=os.path.dirname(path)
        grand_path=os.path.join(parent_path,self.file_name)

        if '\..' in grand_path:
            final_path=grand_path.replace('\../','/')
        return final_path
    #读取文件
    def read_file(self):
        path=self.get_path()

        if  'yaml'in self.file_name:
            print(path)
            with open(path, 'rb') as pf:
                data=load(pf)
            return data
        elif 'ini' in self.file_name:
            config=ConfigParser()
            config.read(path)
            return config


if __name__=='__main__':
    op =operate_File('../TestData/gm/valid.yaml')
    d=op.read_file()
    check_data={
            'test_name':'用户信息查询',
            'parm':{
                'service':'bind_url',
                'body':{
                    'index':{
                        'name':'shen',
                        'vals':[111111,222222]
                    }
                    }
                },
            'expect':[{
                'parm.body.index.name':'wang'
            }]
            }


    print(d)
    print(check_data)
    expect_data = d.get('expect')[0]
    key,=expect_data

    li = key.split('.')

    for x in range(len(li)):
        d = d.get(li[x])
    expect_str = expect_data.get(key)

    print('')




