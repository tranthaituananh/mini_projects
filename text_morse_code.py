from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

print('----------- TEXT <-> MORSE CODE ----------')
print('--- Made with ♥️ by Tran Thai Tuan Anh ---')

#text to morse code
def text_to_morse_code(text):
    morse_code = {
        'A':'.-',
        'B':'-...',
        'C':'-.-.',
        'D':'-..',
        'E':'.',
        'F':'..-.',
        'G':'--.',
        'H':'....',
        'I':'..',
        'J':'.---',
        'K':'-.-',
        'L':'.-..',
        'M':'--',
        'N':'-.',
        'O':'---',
        'P':'.--.',
        'Q':'--.-',
        'R':'.-.',
        'S':'...',
        'T':'-',
        'U':'..-',
        'V':'...-',
        'W':'.--',
        'X':'-..-',
        'Y':'-.--',
        'Z':'--..',
        '1':'.----',
        '2':'..---',
        '3':'...--',
        '4':'....-',
        '5':'.....',
        '6':'-....',
        '7':'--...',
        '8':'---..',
        '9':'----.',
        '0':'-----',
        ', ':'--..--',
        '.':'.-.-.-',
        '?':'..--..',
        '/':'-..-.',
        '-':'-....-',
        '(':'-.--.',
        ')':'-.--.-'
    }
    morse_code_text = ''
    for letter in text:
        if letter != ' ':
            morse_code_text += morse_code[letter] + ' '
        else:
            morse_code_text += ' '
    return morse_code_text

#morse code to text
def morse_code_to_text(morse_code):
    morse_code_dict = {
        '.-':'A',
        '-...':'B',
        '-.-.':'C',
        '-..':'D',
        '.':'E',
        '..-.':'F',
        '--.':'G',
        '....':'H',
        '..':'I',
        '.---':'J',
        '-.-':'K',
        '.-..':'L',
        '--':'M',
        '-.':'N',
        '---':'O',
        '.--.':'P',
        '--.-':'Q',
        '.-.':'R',
        '...':'S',
        '-':'T',
        '..-':'U',
        '...-':'V',
        '.--':'W',
        '-..-':'X',
        '-.--':'Y',
        '--..':'Z',
        '.----':'1',
        '..---':'2',
        '...--':'3',
        '....-':'4',
        '.....':'5',
        '-....':'6',
        '--...':'7',
        '---..':'8',
        '----.':'9',
        '-----':'0',
        '--..--':', ',
        '.-.-.-':'.',
        '..--..':'?',
        '-..-.':'/',
        '-....-':'-',
        '-.--.':'(',
        '-.--.-':')'
    }
    text = ''
    for letter in morse_code.split(' '):
        if letter != '':
            text += morse_code_dict[letter]
        else:
            text += ' '
    return text

while(1):
        print('1. Text to Morse Code', '\n2. Morse Code to Text', '\n3. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            text = input('Enter text to convert to morse code: ')
            print(text_to_morse_code(text.upper()))
        elif choice == 2:
            morse_code = input('Enter morse code to convert to text: ')
            print(morse_code_to_text(morse_code))
        elif choice == 3:
            print('Goodbye!')
            exit()
        else:
            print('Invalid choice')
