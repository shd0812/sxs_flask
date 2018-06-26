from Common.common_Time import hh_Time
import hashlib
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import string
import random
import json
import struct
from Common.common_Logger import myLog

logger = myLog.getLog()

#生成16位随机字符串
def creat_salt_string():

    return  ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

# 获取密钥
def create_RegKey():
    # 谷米分配的密钥
    secret='12345678SXS23Jlsjll233562'
    #获取时间戳
    hh = hh_Time()
    timeStamp = str(hh.getTimestamp())

    before_regKey=secret+timeStamp

    before_regKey_byte= bytes(before_regKey,encoding='utf-8')
    logger.buildStartLine_info('md5加密前%s' % before_regKey_byte)
    regKey=hashlib.md5(before_regKey_byte).hexdigest()[8:-8]

    logger.buildStartLine_info('md5加密后%s' % regKey)
    return  regKey

class ase_GuMi():
    def __init__(self):
        self.key = create_RegKey().encode(encoding="utf-8")
        self.mode = AES.MODE_CBC
        #self.iv=creat_salt_string().encode(encoding="utf-8")

    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        logger.buildStartLine_info('key和iv为%s' % self.key)
        cryptor = AES.new(self.key, self.mode, self.key)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            text = text + ('\0' * add)
        elif count > length:
            add = (length - (count % length))
            text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text.encode())
        logger.buildStartLine_info('ase加密后的数据为：%s' %str(b2a_hex(self.ciphertext), 'utf-8'))

        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return str(b2a_hex(self.ciphertext), 'utf-8')

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):

        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text

#获取要加密的数据
def get_RawData(data):
    RandomStr = creat_salt_string()
    data = json.dumps(data)
    DataLength = struct.pack('I', len(data))
    PlatId = 'SXS'
    RawData = RandomStr + DataLength.decode() + data + PlatId
    return RawData


#获取签名
def create_Sign(EncryptData):
    Token='shaxiaosengdevcode'
    Nonce='sxsn'
    hh = hh_Time()
    timeStamp = str(hh.getTimestamp())

    result_li=[EncryptData,Token,timeStamp,Nonce]
    logger.buildStartLine_info('获取签名排序前:%s' %result_li)
    result_li.sort()
    logger.buildStartLine_info('获取签名排序后:%s' % result_li)
    sort_str=''
    for k in result_li:
        sort_str+=k

    data = hashlib.sha1(sort_str.encode('utf-8')).hexdigest()
    logger.buildStartLine_info('签名；%s' %data)
    return data


if __name__ =='__main__':
    ase = ase_GuMi()
    s=ase.encrypt('1213132')
    #print(s)
    create_RegKey()
    create_Sign(s)



