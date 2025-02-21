# A simple Fibonacci Series:
#fibonacci series always starts with 0&1 , where each number is the sum of before 2 numbers.

user_input = int(input("enter the number until the series you want: "))

x=0     
y=1
print(x)
print(y)

for i in range(1,user_input+1):
    a = x+y
    x = y
    y = a
    print("here is your fibonacci series:- ",a)