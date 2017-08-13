# I am going to make a number guessing game
import random

myname = (input("Hey buddy!! What is your name\n"))
myname = myname.upper()
s = 'Welcome {} how about a number guessing game'.format(myname)
print(s)
print('So here you will be given maximum 5 chances to guess the number\n')

guesses = 0
computers_number = random.randint(1, 20)

# now this loop is going to be executed 5 times in row until correct guess.
while guesses < 6:
    guessed_number = int(input('Take a guess\n'))
    guesses += 1

    if guessed_number is computers_number:
        n = 'You guessed it correctly, number was {} '.format(guessed_number)
        print(n)
        break
    elif guessed_number < computers_number:
        print('Your guess was higher then the number that I thought for you\n')
    elif guessed_number > computers_number:
        print('Your guess was lesser then the number that I thought for you\n')
 
 
if guessed_number != computers_number:
    p = 'I was actually thinking of {}'.format(computers_number)
    print(p)
    print('\n')
    print('Your 5 chances are exhausted better luck next time\n')
