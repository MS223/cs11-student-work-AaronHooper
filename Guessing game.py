range= input('pick a range')
guess = input ('pick a number within that range')
score = 0
import random
random_number = (random.randint(1,range))
"""add a while loop"""
while guess != random_number:
    if guess < random_number:
       score= score + 1
       print "Guess a little higher"
       guess= input ('guess again')
    elif  guess > random_number:
       score = score + 1
       print "guess a little lower"
       guess= input ('guess again')
print "you guessed it fam"
print "The amount of times you failed i mean guessed is " + str(score)
