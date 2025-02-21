#Username & password login using nested if concept:
user_name=input("Enter username: ")
passwd=input("Enter Password: ")
if user_name=="Admin":
    if passwd=="preethi":
        print("Login successful")
    elif passwd=="1234":
        print("your password is weak")
    else:
        print("Password Incorrect!!,Please print Correct password")
elif user_name=="Guest":
    if passwd=="Guestuser":
        print("Login successfull")
    elif passwd=="1234":
        print("your password is weak")
    else:
        print("Password Incorrect!!,Please print Correct password")

else:
    print("Incorrect username , Please try again..!")