from Common.common_Time import hh_Time
import hashlib
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
# 获取密钥
def create_RegKey():
    # 谷米分配的密钥
    secret='dfadfsadfsdaf'
    #获取时间戳
    hh = hh_Time()
    timeStamp = str(hh.getTimestamp())

    before_regKey=secret+timeStamp

    before_regKey_byte= bytes(before_regKey,encoding='utf-8')
    print(before_regKey_byte)
    regKey=hashlib.md5(before_regKey_byte).hexdigest()

    print('md5加密%s' % regKey)
    return  regKey

class ase_GuMi():
    def __init__(self):
        self.key = b'sxsadjgdAkg_llhs'
        self.mode = AES.MODE_CBC


    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text,iv=b'sxsadjgdAkg_llhs'):
        # print(text)
        cryptor = AES.new(self.key, self.mode, iv)
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
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return str(b2a_hex(self.ciphertext), 'utf-8')

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text,iv=b'sxsadjgdAkg_llhs'):
        print(type(self.key))
        cryptor = AES.new(self.key, self.mode, iv)
        plain_text = cryptor.decrypt(a2b_hex(text))
        print(plain_text.decode())
        return plain_text.decode()

#获取签名
def create_Sign(EncryptData):
    Token='sxst'
    Nonce='sxsn'
    hh = hh_Time()
    timeStamp = str(hh.getTimestamp())

    result_li=[EncryptData,Token,timeStamp,Nonce]
    print('排序前:%s' %result_li)
    result_li.sort()
    print('排序后:%s' % result_li)
    sort_str=''
    for k in result_li:
        sort_str+=k

    data = hashlib.sha1(sort_str.encode('utf-8')).hexdigest()
    print('签名；%s' %data)
    return data


if __name__ =='__main__':
    ase = ase_GuMi()
    s=ase.encrypt('1213132',b'sxsadjgdAkg_2lhs')
    #print(s)
    create_Sign('123123')
