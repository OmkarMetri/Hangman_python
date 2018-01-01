import os
from random import randint

def clearscr():
    if os.name == 'posix':
        os.system('clear')
    else :
        os.system('cls')


countries = open('countries')
countries = countries.read()
countries = [x for x in countries.split('\n') if x!='']
country = countries[randint(0,len(countries))]

print(country)

emp_string = ''
for x in country:
    if x!= ' ':
        emp_string = emp_string + '_'
    else:
        emp_string = emp_string + ' '

print(emp_string)

trials = 6

clearscr()

print('''
                            Let's play Hangman!
                You get 6 chances to guess the right country name
                          Press Enter to continue
''')
input()
clearscr()

win = 0
entered = ''

while trials!=0 and win!=1:
    print('''
                    %s \n\n
                    Trials Left: %d\n\n

    ''' %(emp_string,trials))
    print('Entered Characters:'+entered)
    guess = input('Enter a character:')
    while (len(guess)!=1 or (not str.isalpha(guess))):
        guess = input('Invalid Input!\nEnter a character:')
    if guess in entered:
        clearscr()
        print('         Character Already Present! Enter a Differernt Character!            ')
    elif guess.lower() in country.lower():
        entered = entered + guess.lower()
        lis = list(emp_string)
        for i in range(len(country)):
            if country[i].lower() == guess.lower():
                lis[i] = country[i]
        emp_string = ''.join(lis)
        clearscr()
    else:
        entered = entered + guess.lower()
        trials = trials - 1;
        clearscr()
    if '_' not in emp_string:
        win = 1
clearscr()
if trials==0:
    print('Better Luck Next Time\nThe country was '+country)
if win ==1:
    print('You win!')
