import hashlib
import sys
import os
import time
import getpass
import random
import string

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
clear();
print('----------- HASHING PASSWORDS ----------')
print('--- Made with ♥️ by Tran Thai Tuan Anh ---')

def hashing_passwords():
    print('Enter your password to hash: ')
    password = getpass.getpass()

    print('Your password is: ' + password)
    print('MD5 is: ' + hashlib.md5(password.encode()).hexdigest())
    print('SHA-1 is: ' + hashlib.sha1(password.encode()).hexdigest())
    print('SHA-224 is: ' + hashlib.sha224(password.encode()).hexdigest())
    print('SHA-256 is: ' + hashlib.sha256(password.encode()).hexdigest())
    print('SHA-384 is: ' + hashlib.sha384(password.encode()).hexdigest())
    print('SHA-512 is: ' + hashlib.sha512(password.encode()).hexdigest())

hashing_passwords()
