# This is a guess the number game.
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# Ask the plater to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess.')
    try:
        guess = int(input())
        if guess < secretNumber:
            print('Your guess is too low,')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break #this condition is the correct guess!
    except ValueError:
        print('Input only number !!!');
        
   # guess = int(input())
try:
    if guess == secretNumber:
        print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
    else :
        print('Nope. The number i was thinking of was ' + str(secretNumber))
except NameError:
    print('Nope. The number i was thinking of was ' + str(secretNumber))
