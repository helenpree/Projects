#here I used random module to get random number until the number given by user.
#And also while loop it runs until it become false.
#And if else condition to check the number is above or below.
import random
print("WELCOME TO PREETHI'S NUMBER GUESSING GAME:)")
t=input("TYPE A NUMBER: ")
if t.isdigit():
    t=int(t)
    if t<=0:
        print("PLEASE TYPE A NUMBER NEXT TIME:(")
        quit()
else:
    print("PLEASE TYPE A NUMBER NEXT TIME:(")
    quit()

random_number=random.randint(0,t)
guess=0
while True:
    guess=guess+1
    user_guess=input("MAKE A GUESS: ")
    if(user_guess.isdigit()):
        user_guess=int(user_guess)
    else:
        print("please enter a number:(")
        continue
    if(user_guess==random_number):
        print("YOU GOT IT YAAR")
        break
    elif(user_guess>random_number):
        print("you are above the number")
    else:
        print("you are below the number")
print("you got in", guess , "guesses")
print("THANK YOU FOR PLAYING:)")



