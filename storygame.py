#Animal game:
#Here i have used Nested if elif else conditions to make story more interested where user never gets bored..:)
name=input("Enter name: ")
print("Welcome",name)
que=input("Do you want to play adventure earth game click (yes/no)").lower()
if que=="yes":
    animal=input("What kind of animal you want to be(tiger/lion/dinosaur)").lower()
    if animal=="tiger":
        print("Runn....... chase deer, rabit,hipotamas,birds all is yourss prey now:))")
        chase=input("Do you want to Hunt/Sleep").lower()
        if chase=="hunt":
            print("Omg you caught a deer, Enjoyy your meals..:)")
        else:
            print("Have a Happy nap...!")
    elif animal=="lion":
        print("You chose the power full animal hahahah!!!")
        print("You are the king of animals, Now you own the forest...!:)")
        chase2=input("Do you want to Own the forest/Sleep for a while").lower()
        if chase2=="own":
            print("You got all animals as your slaves...:)WOwwww.. Enjoy owning the forest")
        else:
            print("Take a Deep Nap King...:).byee")
    elif animal=="dinosaur":
        print("OMG you are the rare species of Animal")
        print("You are the most scariest animal on forest and earth")
        chase3=input("Do you want to kill/sleep").lower()
        if chase3=="kill":
            print("You caught tiger , rabbit, sheep...Enjoy your Dinner:)")
        else:
            print("Take a deep sleep...byee")

else:
    print("Okayy... Tata bye byee..:)")