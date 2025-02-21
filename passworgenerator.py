#here i importe random module to get random password options:
import random
user=int(input("Enter length of password you want: ")) 

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()_+/*\\|<>;:"

password = "" 

for i in range(user):
    password+=random.choice(chars)
print(password)