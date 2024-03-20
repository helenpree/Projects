#variable assignings:
s_username="Preethi"
s_password="helen"
#getting inputs from user:
uname = input("Enter username:")
password = input("Enter password:")
def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False
a=validate()
print(a)
