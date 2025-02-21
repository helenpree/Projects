#Rock,paper,scissor game
choices=["rock","paper","scissor"]
while True:
    name1=input("Enter your name: ")
    name2=input("Enter your name: ")
    player1=input("Enter your option from : ").lower()
    player2=input("Enter your option from choices: ").lower()
    if player1==choices[0] and player2==choices[2]:
        print(f"{name1} winsss:)")
    elif player1==choices[1] and player2==choices[0]:
        print(f"{name1} winsss:)")
    elif player1==choices[2] and player2==choices[1]:
        print(f"{name1} winsss:)")
    else:
        print(f"{name2} Winss:) ")
    check=input("Do you want to play again: ")
    if check=="quit":
        break
    elif check=="yes":
        continue
