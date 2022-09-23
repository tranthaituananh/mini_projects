import PyPDF2
import os
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

try:
    import PySimpleGUI as sg
    from pytube import YouTube
except ImportError:
    os.system("pip install PyPDF2")

print('---------- Convert PDF to TXT -----------')
print('--- Made with ♥️ by Tran Thai Tuan Anh ---')

if(os.path.isdir("temp") == False):
    os.mkdir("temp")
    
txt_path = ""
pdf_path = ""

#Provide the path for your pdf and txt here
pdf_path = input("Enter the name of your pdf file - please use backslash when typing in directory path: ")   
txt_path = input("Enter the name of your txt file - please use backslash when typing in directory path: ")   

BASEDIR = os.path.realpath("temp") # This is the sample base directory where all your text files will be stored if you do not give a specific path
print(BASEDIR)
print('-' * 70, 'START!', '-' * 70)
if(len(txt_path) == 0):
    txt_path = os.path.join(BASEDIR,os.path.basename(os.path.normpath(pdf_path)).replace(".pdf", "")+".txt")
pdf_obj = open(pdf_path, 'rb')

pdf_read = PyPDF2.PdfFileReader(pdf_obj)

x = pdf_read.numPages

for i in range(x):
    pageObj = pdf_read.getPage(i)
    with open(txt_path, 'a+') as f: 
        f.write((pageObj.extractText()))
    print(pageObj.extractText()) #This just provides the overview of what is being added to your output, you can remove it if want

pdf_obj.close()
print('-' * 70, 'DONE!', '-' * 70)
