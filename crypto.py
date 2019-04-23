#!/usr/bin/env python
#----------------------PART-1-----------
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
#-----------------------PART-2-----------
salt = 'E\x17V\x0c\x86\x0b\xa7\x0b\xe8#\xb9$9\xeeg\xd6'
#----------------------------------------
password = raw_input("Enter the password:")
password1 = password.encode()
kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length    = 32,
        salt      = salt,
        iterations= 100000,
        backend   = default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password1))
print "This is the key:",key

#----------------------Encoding the message-------------

with open("/root/Desktop/Crypython/data.txt",'r') as p:
    message = p.read()
    encoded = message.encode()
    p.close()
    print "this is encoded message:",encoded
#----------------------Encrypt the message----------

f = Fernet(key)
encrypted = f.encrypt(encoded)
print "this is encrypted message", encrypted


with open('/root/Desktop/Crypython/data.txt','w') as data2:
    data2.write(encrypted)
    data2.close()

