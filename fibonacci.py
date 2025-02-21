# A simple Fibonacci Series:
#fibonacci series always starts with 0&1 , where each number is the sum of before 2 numbers.
#Fibocci series until the user given series:
u=int(input("enter num: "))
i=0
ft=0
sc=1
if u==0:
    print(0)
elif u==1:
    print(0,1)
else:
    i=2
    print(ft)
    print(sc)
    while i<=u:
        x=ft+sc
        ft=sc
        sc=x
        print(x)
        i+=1