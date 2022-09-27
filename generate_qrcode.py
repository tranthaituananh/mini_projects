import qrcode
from os import name, system

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()

print("-" * 37, "QR Code Generator", "-" * 37)
print("-" * 30, "Made with ♥️ by @tranthaituananh", "-" * 30)

while(1):
    try:
        choose = input("1. Generate QR Code \n2. Exit \nChoose: ")

        if choose == "1":
            data = input("Enter data: ")
            img = qrcode.make(data)
            img.save("qrcode.png")
            print(" → QR Code saved as qrcode.png")
        elif choose == "2":
            print(" 👋 Goodbye!")
            exit()
        else:
            raise Exception
    except Exception:
        print(" ❌❌❌ Error! Please try again! ❌❌❌ ")
