#Practice questions from cpileraninghub.com
# for practice purpose - Pattern questions:
#To print in square format:
n=5
for i in range(1,n+1):   #this range is to print rows
    for j in range(n):     #this range is to print stars/columns
        print(" * ",end="")
    print(" ")
l=3
for i in range(l):    #3 rows
    for j in range(6):   #6 dollars
        print("$",end=" ")
    print(" ")
#Increasing triangle:
x=5
for i in range(1,x+1):
    for j in range(1,i+1):
        print("#",end=" ")
    print("")
 
 #Decreasing triangle:
for i in range(1,x+1):
    for j in range(i,x+1):
        print("^",end=" ")
    print(" ")
        
#Right triangle:-it needs on decreasing spacing triangle and increasing printed triangel:
print("RIGHT TRIANGLE")
n=5
for i in range(n+1):
    for x in range(i,n+1):
        print(" ",end=" ")
    for y in range(1,i+1):
        print("*",end=" ")
    print()

#Left triangle : it needs increasing spacing triangle and decreasing printing triangle"
print("LEFT TRIANGLE")
l=5
for a in range(l+1):
    for i in range(1,a+1):
        print(" ",end=" ")
    for j in range(a,l+1):
        print("*",end=" ")
    print()

#Captical alphabetic pattern
l=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(l),end=" ")
        l+=1
    print()

#another simple method:
for i in range(1,6):
    print(str(i)*i)
for i in range(1,6):
    print((10**i-1)//9*i)