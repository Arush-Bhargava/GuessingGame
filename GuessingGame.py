from itertools import count
import random
choice = 5
rno= random.randrange(1,9)
print(rno)


while (choice>0):
    guess = int(input("Enter your guess here : "))
    if (guess > rno):
        print("Maybe a little bit lower?")
        choice = choice-1
        print(choice)   
    elif (guess < rno):
        print("Uh! just a little higher?")
        choice = choice-1
        print(choice)
    else:
        print("Congrats! YOU WIN by guessing the right no")
        choice = 0
else:
    print("GameEnd")