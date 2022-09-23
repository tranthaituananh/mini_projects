from os import system, name 
import random

print('----------- GUESS THE NUMBER ------------')
print('--- Made with ♥️ by Tran Thai Tuan Anh ---')

def guess(x):
    #random from 0->x
    random_number = random.randint(0, x)
    guess = 0
    while guess != random_number:
        #Enter the number you guessed
        guess = int(input(f'Guess a number between 0 and {x}: '))
        
        #The number you entered is lower than the result
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        #The number you entered is higher than the result
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    
    #Clean terminal   
    def clear(): 
        # for windows os
        if name == 'nt': 
            _ = system('cls') 
    
        # for mac and linux os
        else: 
            _ = system('clear')     
    clear()

    #You guess the correct result
    print(f'Yah, Congratulations, you guessed correctly! The number to look for is: {random_number}')
        
global x
#Enter the number you want to guess
x = int(input('Input X (0->X): '))
guess(x)
