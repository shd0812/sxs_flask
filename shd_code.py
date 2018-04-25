import base64
import binascii
def sxs_xor(orig, seed):
    dest = []
    rate = len(orig) // len(seed)
    smod = len(orig) % len(seed)#6
    new_seed = seed * rate + seed[0:smod]
    # print(enumerate(orig))
    # print(orig.decode("utf8"))
    for i, x in enumerate(orig.decode("utf8")):
        o = chr(ord(x) ^ ord(new_seed[i]))
        dest.append(o)
    return "".join(dest)

def encryt_sxs(orig, seed):
    """加密方法：base64，异或，16进制"""
    new_orig=bytes(orig, encoding="utf8")
    bstr = binascii.hexlify(new_orig)
    enstr = sxs_xor(bstr, seed)
    new_enstr=bytes(enstr, encoding="utf8")
    test_enstr = base64.b64encode(new_enstr)
    # print("test_enstr>>>>>>>>>>>", test_enstr,type(test_enstr))  wvPWMCjFLagdzg wBdbgvR    px0xiW
    new_enstr=test_enstr.decode("utf8")
    return new_enstr
def decrypt_sxs(dest, seed):
    """解密方法:base64,异或,16进制"""
    enstr = base64.b64decode(dest)
    bstr = sxs_xor(enstr,seed)
    hex_bstr= binascii.unhexlify(bstr)
    a = str(hex_bstr, 'ascii')
    return a
	
if __name__ =='__main__':
		
	s = 'XXZ6WVEiTCJcc38lVFVJVFlzf1NUVUlWWXV/VlRTSV5ZdX5XUFFNVFxze1NQVE1QXHJ/JVRVSVZZd39QVFVJVlhweiNRXUxTWQJ6WFMiT1RfAHpVVFFMU1lzeldUUElWXHJ/UVRXSVVZd39TUVJJXll3elBUUElUXHN6V1RSSVZZdn9ZVFVMU1lzf1NRUElfXHV+V1EgTFZcdX8lUV1PV1x+eidRIUxSWHZ/V1BX'
	dd='{"code":100,"num":1,"data":[{"id":"238","title":"\u5173\u4e8e\u65b0\u7f51\u94f6\u884c\u5b58\u7ba1\u7cfb\u7edf\u6b63\u5f0f\u4e0a\u7ebf\u7684\u516c\u544a"}]}'
	
	key = 'jFLagdzg'
	key2 = 'Gs18dMSP'
	print(encryt_sxs(dd,key2))
	print (decrypt_sxs(s,key))
	# ss = '{"code":100,"num":1,"data":[{"id":"238","title":"\u5173\u4e8e\u65b0\u7f51\u94f6\u884c\u5b58\u7ba1\u7cfb\u7edf\u6b63\u5f0f\u4e0a\u7ebf\u7684\u516c\u544a"}]}'
	# print enc(ss,key2)
	
