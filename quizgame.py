#here i used if else condition: if is "true" it prints out the if printing part otherwise it prints else printing part.
#here you need to answer such basic knowledgable questions and you can get your score based on ur answers.
print("WELCOME TO QUIZ GAME")
a=input("DO YOU WANT TO PLAY? ").lower()
score=0
if(a=="yes"):
    print("LETS PLAY :)")
else:
    print("BYEE")
    quit()

b=input("who is founder of python? ")
if(b.lower() == "guido van rossum"):
    print("CORRECT!")
else:
    print("WRONG")
    score=score+1

c=input("Is python is interpreter or compiler program? ")
if(c.lower()=="interpreter"):
    print("CORRECT")
else:
    print("WRONG")
    score=score+1

d=input("what is cpu stand for? ")
if(d.lower()=="central processing unit"):
    print("CORRECT")
else:
    print("INCORRECT")
    score = score + 1

e=input("what is GUI stands for? ")
if(e.lower()=="graphical user interface"):
    print("CORRECT")
else:
    print("INCORRECT")
    score=score+1


f=input("what is IDE stands for? ")
if(f.lower()=="integrated development environment"):
    print("CORRECT")
else:
    print("INCORRECT")
    score=score+1

print("You got", (score/5)*100, "%")









