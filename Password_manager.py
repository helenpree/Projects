def view():
    with open("Password.txt","r") as f:
        f.readlines()
def add():
    acc_name=input("enter account name: ")
    pwd=input("Enter password: ")
    with open("Password.txt","a") as f:
        f.write(acc_name+ "|" +pwd+"\n")
while True:
    que=input("would you like to (add/view) the password or click q to quit: ").lower()
    if que=="q":
        break
    if que=="add":
        add()
    elif que=="view":
        view()
    else:
        print("Please enter the valid option:(")
        continue
