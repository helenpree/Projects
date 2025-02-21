print("*****MINI CALCULATOR****")
def add(x,y):
    a=x+y
    print("THe Addition of x and y is: ",a)
def sub(x,y):
    b=x-y
    print("THe Subtraction of x and y is: ",b)
def div(x,y):
    c=x/y
    print("THe Division of x and y is: ",c)
def mul(x,y):
    d=x*y
    print("THe Multiplication of x and y is: ",d)  
i=int(input("Enter num1:"))
j=int(input("Enter num2:"))
user_que=input("Choose add/mul/div/sub: ")
if user_que=="add".lower():
    print(add(i,j))
elif user_que=="sub".lower():
    print(sub(i,j))
elif user_que=="div".lower():
    print(div(i,j))
else:
    print(mul(i,j))