import random
import os
from os import system, name 

#Clean terminal 
def clear(): 
    # for windows os
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux os
    else: 
        _ = system('clear')     
clear()

try:
    import pyperclip 
except ImportError:
    os.system("pip install pyperclip")

print('---------- PASSWORD GENERATOR -----------')
print('--- Made with ♥️ by Tran Thai Tuan Anh ---')

symbol = 0
lower = 0
upper = 0
number = 0
count = 0
password = []

length = input("\nHey, Welcome. Enter the number of characters you want to use for the password (default 128): ")
length = 128 if length is '' else int(length)

#Randomly select ascii character classes and individual characters
while count < length:
    rand = random.randint (0,3)
    if rand == 0:
        lower += 1
        b = int(random.randint (97,123))
        password.append(b)
    elif rand == 1:
        upper += 1
        b = random.randint (65,91)
        password.append(b)
    elif rand == 2:
        number += 1
        b = random.randint (48,58)
        password.append(b)
    elif rand == 3:
        r = random.randint(0,2)
        symbol += 1
        if r == 0:
            b = random.randint (33,48)
            password.append(b)
        elif r == 1:
            b = random.randint (91,97)
            password.append(b)
        elif r == 2:
            b = random.randint (123,126)
            password.append(b)
    count += 1
        
#Convert ascii code to characters
your_password = "".join([chr(c) for c in password])

#Copy password to clipboard
pyperclip.copy(your_password)

#Print the result
print ("\nYour random password of length is %s including" % length, lower,"lowercase,",upper,"uppercase,",number,"numbers and",symbol,"symbol characters\n")

print('*' *35, 'YOUR RANDOM PASSWORD','*' *35)
print('\n',your_password, '\n')
print('*' *92)

print ("\n* NOTICE: YOUR PASSWORD COPIED TO CLIPBOARD\n")
