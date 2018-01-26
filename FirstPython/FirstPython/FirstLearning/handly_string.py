#Multiline Strings with Triple Quotes
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
print('----------------------------')
#Use esc charter
print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')
print('----------------------------')
print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper())
print('HELLO'.lower())
print('HELLO'.lower().islower())
print('----------------------------')

#The join() and split() String Methods
print('My name is Simon'.split('is'),sep=';')
print('----------------------------')
#Justifying Text with rjust(), ljust(), and center()
print('Hello'.rjust(20, '*'))
print('Hello'.center(20, '='))
#Removing Whitespace with strip(), rstrip(), and lstrip()
spam = ' Hello World       '
print(spam,end='')
print('Remove Whitespace:',spam.strip())
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam)
print('Remove ampS in string:',spam.strip('ampS'))
print('----------------------------')
#string check value
import sys
sys.exit()
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        print(password.isalnum())
        break
    print('Passwords can only have letters and numbers.')
    
print('----------------------------')
