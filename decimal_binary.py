from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear();
print('----------- DECIMAL <-> BINARY ----------')
print('--- Made with ♥️ by Tran Thai Tuan Anh ---')

while(1):
    try:
        menu = int(input("\nChoose an option: \n 1. Decimal to binary \n 2. Binary to decimal \n 3. Exit \n Option: "))
        if menu == 1:
            dec = int(input("\nInput your DECIMAL number:\nDECIMAL: "))
            print("BINARY: {}".format(bin(dec)[2:]))
        elif menu == 2:
            binary = input("\nInput your BINARY number:\n BINARY: ")
            print("DECIMAL: {}".format(int(binary, 2)))
        elif menu == 3:
            print("Goodbye!")
            exit()
        else:
            raise ValueError
    except ValueError:
        print ("Please choose a valid option!")
