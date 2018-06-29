from Common.common_Time import hh_Time
import hashlib
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

from Common.common_Logger import myLog
from Common.common_OpFile import operate_File
logger = myLog.getLog()



def get_ParmData(path):
    op =operate_File(path)
    d=op.read_file()
    return d.get('parm')

if __name__ =='__main__':
    get_ParmData('')



