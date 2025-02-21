#1.print only positive numers in a list:
list1=[23,45,-9,-8,-7,-92,87,67,55,-45]

for i in list1:
    if i > 0:    #less than zero are negative numbers
      print("positive integers are ",i)


#2.positive numbers count:
count=0
for j in list1:
   if j >0:
      count+=1
print("Count of positive integers are ",count)

#3.Negative numbers count
a=0
for k in list1:
   if k < 0:
      a+=1
print("Count of negative integers are ",a)

#4. sum of even numbers 
n=10
sum=0
for i in range(1,n+1):
   if i%2==0:
      sum=sum+1
print("Even count ",sum)
      
#5.odd numbers count:
user_input=10
odd_count=0
for k in range(user_input):
   if k %2!=0:
      odd_count+=1
print("Odd numers count are ",odd_count)
      
#6.Mutliplication table:
table_num=7
for i in range(1,11):
   print(table_num,"*",i,"=",i*table_num)
#using while loop:
add=1
while add<11:
   print(table_num*add)
   add+=1

#7.Factorial calculator:
fact=5
add=1
for x in range(1,5+1):
   add=add*x

print("factorial",add)
#using while loop:
user=6
var=1
x=1
while x<=user:
   var=var*x
   x=x+1
print(var)

#8.input asking again and agian using while loop:
while True:
    a=int(input("1-10: "))
    if a>=1 and a<=10:
        print("thank you")
        break
    else:
        print("please enter valid number")
        
#9.Prime num checker:
#Prime number :- it cannot be divided by any other whole number\
# other than itself eg:2,3,7,11,5.
num=7
for i in range(2,num):
    if num%i==1:  
        print("It is a prime number")
        break
    else:
        print("It is not a prime number")

#10.List uniqueness checker:
items=["apple","banana","grape","apple","orange"]
unique=set()  #set can remove duplicate values in a list
for i in items:
   if i in unique:
      print("duplicate found ",i)
      break
   unique.add(i)

#11.print numbers from 10-15 using while loop:
num=10
while num<=15:
    print(num,end=" ")
    num+=1
    
#12.finding cube and square of numbers:
for j in range(1,5+1):
    print("cubes of numbers: ",i*i*i)

for i in range(1,5+1):
    print("square of numbers: ",i*i) 
#using while loop: 
num=1
while num<=6:
    print(num*num*num)
    num+=1
   
#13.printing odd numbers using while loop:
num=1
while num<=10:
    if num%2!=0:
        print(num)
    num+=1

#14.product of 1-5 numbers or factorial of 5 using for and while loop:
num=1
var=1
while var<=5:
    num=num*var
    var+=1
print(num)

x=1
for i in range(1,6):
    x=x*i
print(x)
    
#15.seperating consonants and vowels:
count=0
vowels="aeiou"
idx=0
word="Preethi"

while idx<len(word):
    if word[idx].lower() not in vowels and word[idx].isalpha():
        count=count+1
    idx+=1
print("Count of consonants",count)
#Counting vowel counts in sentence:
sentence="Preethi"
add=0
while idx<len(sentence):
    if sentence[idx].lower() in vowels and sentence[idx].isalpha():
        add+=1
    idx+=1
print("Vowel count are: ",add)

#16.print first 5 multiples of 3:
num=3
i=1
while i<=5:
    print(num*i)
    i+=1
#using for loop:
for j in range(1,6):
    print(num*j)

#17.calc 3 to the power of 4:
b=3
e=4
print(b**e) #3 power 4
print(b*e)   #3 x 4

#18.perfect square checker:
num=81
i=1
while i**2<=num:
    if i**2==num:
        print(num ,"is a perfect square of",i)
        break
    i+=1
#19.occurence/count of particular string:
string="preethi"
letter="e"
idx=0
count=0
while idx<len(string):
    if string[idx]==letter:
        count+=1
    idx+=1
print(count,"times","'",letter,"'")
#using string methods
string1="success"
x=string1.count("s")
y=string1.count("c")
print(x)

#20.calculate area od triangle:-formulae A = 1/2 × b × h
b=13
h=90
area_of_triangle=(1/2)*b*h
print(area_of_triangle)

#21.#swap variables:
a=10
b=20
temp_var=a
a=b
b=temp_var
print("value of a is",a)
print("value of a is",b)
#ANother method:
x=90
y=76
x,y=y,x
print("value of x",x)
print("value of y",y)

#22.generate random number: #use random module and randint function

#23.checking +ve or -ve
x=90
if x>0 and x>1:
    print("POsitive")
elif x==0 :
    print("zero")
else:
    print("negative")

#24.odd or even
x=25
if x%2==0:
    print("even")
else:
    print("odd")

#25.check leap year: lap yr=366 days , comes once in 4yrs
    #formula %by 400 and %100 and reminder =0
    #%by 4=0 and %100!=0
x=1996
if x%4==0 and x%100!=0:
    print(f"yes {x} is a leap year")
elif x%400==0 and x%100==0:
    print(f"yes {x} is a leap year")
else:
    print("noo it is not")

#26. finding greatest of all
a=10
b=8
c=32
if a>b and a>c:
    print(f"{a} is grater than b and c.")
elif b>a and b>c:
    print(f"{b} is grater than a and c.")
else:
    print(f"{c}, c is greater")

#27. check prime number:
num=int(input("Enter num "))
id=2

while id<=num:
    if num%id == 0:
        print("not a prime number")
        break
    id+=1
else:
    print(f"{num} is a prime number")
#using for loop:
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print(f"{num} is a prime")
        
#28.findinf factorial using while and for loop:
fact=6
d=1
x=1
while x<=fact:
    d=d*x
    x+=1
print(f"The factorial of {fact} is:",d)
#using for loop
f=7
y=1
for i in range(1,f+1):
    y=y*i
print(y)

#29. Fibonacci sequence: where each number is the sum of two numbers before it.Always start with 0 & 1.
a=0
b=1
num=10
print(a)
print(b)
for i in range(1,num+1):
    c=a+b
    a=b
    b=c
    print(c)
#using while loop:
a=0
b=1
num=8           
x=1
print(a)
print(b)
while x<=num:
    c=a+b
    a=b
    b=c
    print(c)
    x+=1

#30.Sum of integers until user given in sequence order:
num=1
total=0
int1=int(input("entr num: "))
if int1==0:
    print("Please enter a positive number")
else:
    while num<=int1:
        total=num+total
        num+=1
print(total)
#using for loop;
x=0
for i in range(1,int1+1):
    x=x+i
print(x)

#31.powers
#lambda = (funtion,iterable)
n=int(input("Enter: "))
powers=list(map(lambda x : x**2,range(n+1)))
print(powers)
sub=list(map(lambda y:y*2,range(n+1)))
print(sub)

#32.numbers divisible by other numbers:
num=6
for i in range(1,50):
    if i%num==0:
        print(i)

#33. converting decimal to binary ,octal: using built in functions;
bi=23
print(bin(bi))
print(oct(bi))
print(hex(bi))

#34. check ASCII value: using function ord()
c="A"
x="#"
print(ord(c))
print(ord(x))

#35.checking hcf or gcd:
x=int(input("Enter num1:"))
y=int(input("Enter num2:"))
if x>y:
    smallest=x
else:
    smallest=y
for i in range(1,smallest+1):
    if x%i==0 and y%i==0:
        hcf=i
print("Highest common factor is :",hcf)

#36.check factors:
a=int(input("enter num to check factors of number: "))
for i in range(1,a+1):
    if a%i==0:
        print(i)

#37.Simple calculator
n1=int(input())
n2=int(input())
x=int(input("Enter 1 for add , 2 for sub ,3 for mul,4 for div: "))
if x==1:
    print(n1+n2)
elif x==2:
    print(n1-n2)
elif x==3:
    print(n1*n2)
else:
    print(n1/n2)

#38.Transpose a matrix: changing row elements to column elements.
a=[[1,2,3],
   [4,5,6]]
c=[[0,0],
   [0,0],
   [0,0]]
for i in range(len(a)):     #rows=2
    for j in range(len(a[0])):   #column: 0 ,1
        c[j][i]=a[i][j] 
for x in c:
    print(x)   

#39.Palindrome checker:
a=input("Enter a word: ")
if a==a[::-1]:
    print("It is a palindrome bro!!")
else:
    print("Oops , it is not palindrome")

#40. Reversing string:
a=input("Enter a word: ")
x=a[::-1]
print(x)

#41. Removing punctuations from string:
#mehtod1:using inbuilt func isalpha()
word="how'r you bro?,well I'm good yaar!"
for i in word:
    if i.isalpha():
        print(i,end=" ")
#method2:
punc='''!/#$%^&*(){};":[]\?@|'''
str1=input("ENter string: ")
empty_str=""
for i in str1:
    if i not in punc:
        empty_str+=i
print(empty_str)

#42.Sorting in alphabetic order:
a="hello bro how are you?"
x=a.split()
for i in range(len(x)):
    x[i]=x[i].lower()
x.sort()
print(x)

#43.Parttern sum:
num=10
for i in range(1,num+1,1):
    for j in range(1,i+1):
        print("*",end="")
    print(" ")

#44.To print sum of numbers until user given:
n=int(input("Enter num:"))
var=0
for i in range(1,n+1):
    var=var+i
print(var)
#using while loop:
num=int(input())
sum=0
i=0
while i<=num:
    sum=sum+i
    i+=1
print(sum)

#45.break > 520 and skip > 150 and print divisible by 5.
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num>520:
        break
    if num>150:
        continue
    if num%5==0:
        print(num)

#46.To reverse and print the list:
list1 = [10, 20, 30, 40, 50]
x=reversed(list1)
for i in x:
    print(i)

#47. to print numbers in reverse range:
for i in range(-10,0):
    print(i)
#using  while loop:
num=-10
while num<0:
    print(num)
    num+=1


#48. Print num lesser than 5 and add in new list using loop:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
for i in a:
    if i>5:
        break
    if i<5:
        b.append(i)
print(b)

#49.print out all divisors of user given number:
a=int(input("Enter num: " ))
b=[]
for x in range(1,a+1):
    if x%a==0:
        b.append(x)
print(b)

#50.To compare lists and remove duplicates:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x=[]
for i in a:
    if i not in b:
        x.append(i)
print(x)
#Another way to print both same and unique items in both list:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
unique_list=[]
rep_list=[]
for x in a:
    if x not in b:
        unique_list.append(x)
    if x in b:
        rep_list.append(x)
print("Unique items",unique_list)
print("Same repeated items",rep_list)

#51.Palindrome another method:
string = list(input("palindrome check: "))
if string == list(reversed(string)):
          print("this is palindrome")
else:
         print("this is not, please try another")

#52.printing even elements in new list:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print(b)
#print both even / odd in seperate list:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list=[]
odd_list=[]
for i in a:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Even elemenets are:",even_list)
print("Odd elements are:",odd_list)

#53.Print squares of given list using list comprehension:
#syntax:- [expression for item in iterable]
sq_list=[1,2,3,4,5,6,7,8,9,10]
x=[]
new_list=[a*a for a in sq_list]
print(new_list)
#-->
sq_list=[1,2,3,4,5,6,7,8,9,10]
cube_list=[1,2,3,4,5,6,7,8,9,10]
new_list=[i*i for i in sq_list]
cubes=[j*j*j for j in cube_list]
print("Squares",new_list)
print("Cubes",cubes)
#using for loop:
for i in sq_list:
    x.append(i*i)
print(x)

#54.Printing odd and even list using lc:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
odd_list=[]
even_list=[]
list1=[i for i in a if i%2!=0]
list2=[j for j in a if j%2==0]
odd_list.append(list1)
even_list.append(list2)
print(odd_list)
print(even_list)

#55.Print similar numbers in both lists using lc:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[i for i in a if i in b]
print(c)
common=[i for i in a for j in b if i==j]
print("Repeated elements:",common)

#56.Print unique numbers :
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[i for i in a if i not in b]
print(c)

#57.printing first and last element
a = [5, 10, 15, 20, 25]
l=len(a)-1
print(a[0::l])

#58.To remove duplictaes using set:
li=[23,23,45,67,76,89,89,3,3,24,100]
y=set(li)
print(list(y))
#using for loop:
li=[23,23,45,67,76,89,89,3,3,24,100]
li2=[]
for x in li:
    if x not in li2:
        li2.append(x)
print(li2)
#using functions:
def duplicate(a):
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    print(new_list)
new_list=[]
list1=[23,34,56,56,7,7,8,9,9,100,100,102,2,3]
duplicate(list1)

#59.Reversing a sentence:
user_input=input("Enter a sentence: ")
x=user_input.split()
y=x[::-1]
print(" ".join(y))

#60.To print only odd numbers in the user range:
user=int(input("enter num: "))
for i in range(1,user):
    if i%2==0:
        continue
    else:
        print(i)
    
#61.To print odd numbers alone in the user range:
user=int(input("enter num: "))
for i in range(1,user):
    if i%2!=0:
        continue
    else:
        print(i)

#62.searching number in list:
list=[48, 4904, 823, 128731, 283, 57, 29, 10, 4765, 348734]
new_list= sorted(list)
user=int(input("enter num to search: "))
for x in new_list:
    if user==x:
        print("number found",x)
        break
else:
    print("Oops not found")

#63.To print decreasing triangle pattern:
n=6
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print(" ")

#64.Printing even mutliples of 5:
x=5
count=0
for i in range(1,11):
    if i%2==0:
        print(x,"*",i,"=",x*i)
        count+=1
print(count)

#65:printing divisibles of 7 between 1-1000:
#using for loop:
for i in range(1,1001):
    if i%7==0:
        print(i)
#using while loop
num=1000
i=1
while i<=num:
    if i%7==0:
        print(i)
    i+=1
#using list comprehension:
new=[i for i in range(1,1000) if i%7==0]
print(new)

#66.Finding 3 in numbers btwn 1-1000.
s=[i for i in range(1,1000+1) if '3' in str(i)]
print(s)

#67. Counting the space in between tjhe string given by user:
strz="excuse me mam shall i get in"
counts=[i for i in strz if i==" "]
print(len(counts))

#68.Printing consonants using list comprehension:
a="Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
vowels='aieou," "'   #include space so it ommit and give output
li=[i for i in a.lower() if i not in vowels]
#li=[i for in a if i in 'aieou," "']
print(li)

#69.To get index , value format use: enumerate function:
items = ["hi", 4, 8.99, 'apple', ('t,b','n')]
result = [(index, item) for index, item in enumerate(items)]
print(result)

#70.Printing only numbers from the string:
sentence="In 1984 there were 13 instances of a protest with over 1000 people attending"
x=sentence.split()
num_list=[i for i in x if i.isnumeric()]
print(num_list)
#To print only alphabets from the sentence:
alpha_list=[j for j in x if j.isalpha()]
print(alpha_list)

#71.Print odd or even list in range(20):
oddoreven_list=["Even" if i%2==0 else "odd" for i in range(1,20+1)]
print(oddoreven_list)

#71.Printing common numbers in both list:
list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2, 7, 1, 12]
new_list=[(a,b) for a in list_a for b in list_b if a==b ]
print(new_list)

#72.Printing letters lesser than 4 and greater than 4:
sentence = 'On a summer day somner smith went simming in the sun and his red skin stunt'
x=sentence.split()
less_than_4=[i for i in x if len(i)<4]
print(less_than_4)
greater_than_4=[j for j in x if len(j)>4]
print(greater_than_4)
   
#73.numbers 1-1000 that are divisible by single digit 2-9: using nested list comprehension:-
num=[ i for i in range(1,1000) if True in[True for j in range(2,9) if i % j == 0]]
print(num)

#74.Printing 10,20,30......300 series order:
for i in range(10,301,10):
    print(i,end=" ")
#using while loop
num=10
var=0
while num<=300:
    print(num,end=" ")
    num+=10

#75.Decreasing series using while loop:
num=100
while num>=7:
    print(num,end=" ")
    num-=7

#76.reverse order:
num=10
while num>=1:
    print(num,end=" ")
    num-=1

#77.Sum of even numbers:
num=1
sum=0
while num<=10:
    if num%2==0:
        sum=sum+num
    num+=1
print("Sum of numbers are: ",sum)

#78.Printing sum of numbers given by user:
user=int(input("Enter num: "))
var1=0
var2=0
while user!=0:
    var1=user%10
    var2=var2+var1
    user=user//10
print(var2)

#79.Printing product of numbers given by user:
user=int(input("Enter num: "))
var1=0
var2=1     #If multiply by everything is zero so using 1.
while user!=0:
    var1=user%10
    var2=var2*var1
    user=user//10
print(var2)

#80.Reversing number given by user:
user=int(input("Enter num:"))
r=0
p=0
while user!=0:
	r=user%10
	p=(p*10)+r
	user=user//10
print(p)

#81. Displaying number names: #using dictionary concept like calling keys it gives value names:-
user=input("Enter num:")
li=list(user)
le=len(li)
idx=0
dict1={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}
while idx<le:
    print(dict1[int(li[idx])])
    idx+=1	

#82.Finding Armstrong number:
f=input("enter number: ")
le=len(f)
lis=list(f)
idx=0
x=0
while idx<le:
    x=x+int(lis[idx])**3
    idx+=1

if int(f)==x:
    print("it is a Armstrong number")
else:
    print("No it is not")

#83.printing numbers till the user given and sum of the digits:
user=int(input("Enter num: "))
sum=0
for i in range(1,user+1):
    print(i)
    sum=sum+i
print("Sum of all integers are: ",sum)

#84.Asking user number again and again and summing them:
ch="yes"
i=0
while ch.lower()=="yes":
    user = int(input("Enter number: "))
    i=i+user
    ch=input("Do you want to continue click(yes/no): ")
print("the sum of digits are:",i)

#85.Counts of positive and negative numbers until user enter zero:
p_count=0
n_count=0
n=1
while n!=0:
    n=int(input("enter num: "))
    if n>0:
        p_count+=1
    else:
        n_count+=1

print("positive numbers: ",p_count)
print("negataive numbers: ",n_count)

#86.checking number palindrome:
num=int(input("Enter a number: "))
x=0
y=0
z=num
le=len(str(num))
i=0
while i<le:
    x= num % 10
    y= (y*10) + x
    num = num // 10
    i+=1
if z == y:
    print("palindrome")
else:
    print("no")

#87.Asking user 10 numbers and giving them average of its number:
i=1
sum=0
while i<=10:
    user=int(input("enter: "))
    sum=sum+user
    i+=1
print("Average: ",sum/10)

#88.Getting 10 numbers from user and finding largest and smallest among them.
i=1
l=[]

while i<=10:
    num=int(input("enter  numz: "))
    l.append(num)
    i+=1
l.sort()
print("largest: ",l[-1])
print("smallest: ",l[0])

#89.Printing odd&even count from n1 to n2 series:
n1=int(input("n1: "))
n2=int(input("n2: "))
odd_sum=0
even_sum=0
if n1>n2:
    while(n2<=n2):
        if n2%2==0:
            even_sum+=n2
            n2+=1
        else:
            odd_sum+=n2
            n2+=1
if n2>n1:
    while(n1<=n2):
        if n1%2==0:
            even_sum+=n1
            n1+=1
        else:
            odd_sum+=n1
            n1+=1
print("odd",odd_sum)
print("even",even_sum)
#same problem using for loop:
n1=int(input("n1: "))
n2=int(input("n2: "))
odd_sum=0
even_sum=0
if n1>n2:
    for i in range(n2+1,n1):
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
if n2>n1:
    for i in range(n1,n2+1):
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
print("odd:",odd_sum)
print("even:",even_sum)

#90.printing 13 divisors but not 3:-
i=101
while i<=500:
    if i % 300 == 0 and i % 3 != 0:
        print(i)
        i+=1

#91.Printing series like 2,22,222,222.....n
n=int(input("Entr number of series you want: "))
i=0
str1='2'
while i<n:
    print(str1,end=",")
    str1+='2'
    i+=1

#92.Printing series of square from 1-10
n=int(input("Enter num: "))
i=1
while i<=10:
    print(i*i,end=",")
    i+=1

#93.printing x,x/1,x^2/2,x^3/3.......x^n/n:
def fact(n):
    f=1
    for j in range(1,n+1):
        f=f*j
    return f
sum=0
i=1
n=int(input("Entr num: "))
x=int(input("Enter num: "))
while i<n:
    sum = sum + x**i/fact(i)
    i+=1
print(sum)

#94.printing sum of cubes of series given by user:
u=int(input("Enter: "))
i=1
sum=0
while i<=u:
    sum=sum+i**3
    i+=1
print(sum)

#95.Printing characters of string
str=input("enter a string: ")
idx=0
while idx<len(str):
    print(str[idx])
    idx+=1
print("total length of string is: ",len(str))

#96.Printining only odd numbers from the list:
l=[20,23,43,45,67,87,89,8,9,10]
new_list=[]

for i in l:
    if i%2!=0:
        new_list.append(i)
print(new_list)
#using while loop
i=0
while i<len(l):
    if l[i]%2!=0:
        print(l[i])
    i+=1

#97. Increasing and decreasing number :
i=1
j=20
while i<=j and j>=i:
    print(i,"-----",j)
    i+=1
    j-=1

#98.Prime checker:
x=int(input())
a=0
if x==1 or x==0:
    a=1
for i in range(2,x):
    if i % x == 0:
        a=1
if a==1:
    print("not a prime")
else:
    print("prime")

#pattern based problem:
n=5
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for a in range(1,n):
    for b in range(a,n):
        print("*",end=" ")
    print()

#99.getting 10 numbers and giving its average using for loop:
sum=0
for i in range(10):
    n=int(input("Et: "))
    sum+=n

print("av",sum/10)

#100.printing divisible of 13 but not 2.
for i in range(100,501):
    if i%11==0 and i%2!=0:
        print(i)
#using while loop:
i=100
while i<=500:
    if i%11==0 and i%2!=0:
        print(i)
    i+=1

#101.Do not print mutliples of 2 & 3.
for i in range(1,21):
    if i%2!=0 and i%3!=0:
      print(i)

#102.getting inputs and givinh its average:
n=1
i=0
sum=0
while n!=0:
    n=int(input("Enter: "))
    sum+=n
    i+=1
print("avg",sum/i)

#103.Perfect number checker: whn the num is equal to sum of its divisors:
num=int(input("enter num: "))
s=0
for i in range(1,num):
    if i % num == 0:
        s=s+i
if s == num:
    print("perfect number!")
else:
    print("no")

#104.Printing alphabetical pattern
l=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(l),end=" ")
        l+=1
    print()

#105Printing each elemnet in str using while & for loop:-
str1="Welcome"
i=0
while i<len(str1):
    print(str1[i])
    i+=1
#using for loop
for x in str1:
    print(x)

#106.Counting length of string without using len function:-
str1="Welcome to my page"
count=0
for i in str1:
    count+=1
print("Total length of the string is:",count)
#using while loop:-
i=0
while i<len(str1):
    i+=1
print(i)

#107.Counting alphabets and digits from the string:
str1="Welcome to my 1st page and 2nd page"
alpha_count=0
num_count=0
for i in str1:
    if i.isalpha()==True:
        alpha_count+=1
    if i.isdigit()==True:
        num_count+=1
print(alpha_count)
print(num_count)

#108.Counting upper and lowercases from the string:
st=input("entr: ")
lc=0
uc=0
for i in st:
    if i.islower()==True:
        lc+=1
    if i.isupper()==True:
        uc+=1
print("lower count: ",lc)
print("upper count: ",uc)

#string methods practice:
#strips concept:
st="hello welcome to my new channel bro"
print(st.lstrip("hel")) #left side
print(st.rstrip("ro"))   #ride side
print(st.strip("welcha"))   #random remove
#istititle(): this function returns true if string contains captials in first letter.
s="hEloo"
d="Wello"
print(s.istitle())
print(d.istitle())
#lower()/upper() and islower()/isupper()
st="lghjs"
x=st.upper()  #to convert
print(x)
print(st.islower()) #is a condition to check is lower or not?
#swapcase():just convert upper to lower and vice versa
r=" welCOme to MY page"
print(r.swapcase())
#split(): split each word by comma and store in list
a="welcome paa"
x=a.split()
print(x)

#109.Displaying each word and its length.
a=input("Entr: ")
a1=a.split()
for i in a1:
    print(i," ","its length is: ",len(i))

#110.Printing string 5 times using loop
st1=input("Entr: ")
for i in range(5):
    print(st1)
#using while loop:
st1=input("Entr: ")    
i=0
while i<=10:
    print(st1)
    i+=1

#111.printing 1st and last element upper.
st="welcomeeee"
x=st[0].upper()+st[1:-2]+st[-1].upper()
print(x)

#112.vowel count:
def vowel_count(st1):
    count=0
    vowels="aieou"
    for i in range(len(st1)):
        if st1[i] in vowels:
            count+=1
    print("vowl count is: ",count)
x=input("entr: ")
vowel_count(x)

#113.
st=input("entr string: ")
x=st.split()
c=0
for i in x:
    c+=1
print(len(x))
print("no of words in string",c)

#114.Counting the alphabets c and a in a string:
st=input("entr: ")
c=0
a=0
for i in st:
    if i == "c":
        c+=1
    if i == "a":
        a+=1
print("count of c",c)
print("count of a",a)

#115.Printing last word from the string:
st=input("entr: ")
x=st.split()
print(x[-1])
#last letter from string:
print(x[-1])

#116.getting users input and adding in list:
veg_list=[]
for i in range(1,6):
    user=input("entr: ")
    veg_list.append(user)
print(veg_list)

#117.Printing odd & even numbers in a new list from users input:
odd_list=[]
even_list=[]
for i in range(1,11):
    user=int(input("entrnum: "))
    if user%2!=0:
        odd_list.append(user)
    if user%2==0:
        even_list.append(user)
print("oddlist",odd_list)
print("evenlist",even_list)

#118.Finding maximum & minimum num from the list:
li=[23,45,67,12,89,99,101]
max=li[0]
min=li[0]
for i in range(len(li)):
    if li[i]>max:
        max=li[i]
    if li[i]<min:
        min=li[i]
print("maximum number: ",max)
print("minimum number: ",min)
#another way:
i.sort()
print(i[-1])

#119.Chcking last igit of the number is divisible by 3.
user_age=int(input("entr: "))
x=user_age%10
if x%3==0:
    print("yes")
else:
    print("no")

#120.Tax amount according to criteria:
price=int(input("entr: "))
tax=0
if price>=100000:
    tax=(15/100)*price
elif price>50000 and price<100000:
    tax=(10/100)*price
elif price<=50000:
    tax=(5/100)*price
print(tax)

#121.Leap year:
yr=int(input("entr year: "))
if yr%4==0 and yr%100!=0:
    print("Leap year")
elif yr%400==0 and yr%100==0:
    print("leap year")
else:
    print("not a leap yr")

#122.Checking user input is 3 digit number:
num=input("entr: ")
s=len(num)

if s==3:
    print("good")
else:
    print("please enter 3 digit number")

#123.checking a person is senior citizen.
age=int(input("entr age: "))
if age>=60:
    print("Senior Citizen")
else:
    print("not a senior citizen")

#124.Finding largest number of 3:
num1=int(input("ent:  "))
num2=int(input("ent:  "))
num3=int(input("ent:  "))
if num1>num2:
    print(num1)
elif num2>num3:
    print(num2)
else:
    print(num3)

#125.percentage to write exams
total_days=int(input("Entr days:"))
absent_days=int(input("Entr days:"))
per=total_days-absent_days/total_days*100
if per>75:
    print("You are eligible for exams")
else:
    print("OOps you are not eligible for exams")

#126.salary increment:
ser=int(input("Entr years of exeprience: "))
salary=int(input("Entr salary: "))
inc=0
if ser>10:
    inc=10/100*salary
elif ser>5 and ser<10:
    inc=8/100*salary
elif ser>3 and ser<5:
    inc=5/100*salary
print(inc)

#127.Discount on sales:
dis=0
final=0
total_amount=int(input("Entr: "))
if total_amount>10000:
    dis=25/100*total_amount
elif total_amount>5000 and total_amount<10000:
    dis=10/100*total_amount
elif total_amount>1500 and total_amount<5000:
    dis=5/100*total_amount
final=total_amount-dis
print(final)

#128.find the type of triangle:
#equivalent triangle: all sides are equal
#scalene triangle: all sies are not equal
#isoceles triangle: atleast 2 sides must be equal.
s1=int(input("entr: "))
s2=int(input("entr: "))
s3=int(input("entr: "))
if s1==s2 and s2==s3:
    print("equilevent triangle")
elif (s1==s2 and s2!=s3)or(s2==s3 and s2!=s1)or(s1!=s3 and s1==s3):
    print("Isoceles triangle")
else:
    print("scalene triangle.")

#129.Accept num & operator from user:
n1=int(input("entr n1: "))
n2=int(input("entr n2: "))
op=input("entr operator: ")
if op=="+":
    print("Addition of n1 & n2 is: ",n1+n2)
elif op=="-":
    print("Subtraction of n1 & n2 is: ",n1-n2)
elif op=="*":
    print("Multiplication of n1 & n2 is: ",n1*n2)
elif op=="/":
    print("Division of n1 & n2 is: ",n1/n2)
else:
    print("Please enter from (+,-,*,/)")

#130.Wages according to criteria:
gender=input("Enter your gender:M/F ").lower()
age=int(input("entr age: "))
no_of_days_worked=int(input("Entr the number of days you worked: "))
if age>=18 and age<30:
        if gender=="F":
                print(no_of_days_worked*700)

        else:
                print(no_of_days_worked*750)
               
elif age>=30 and age<=40:
        if gender=="F":
            print(no_of_days_worked*800)

        else:
                print(no_of_days_worked*850)
else:
        print("Please  enter your appropriate age") 

#131.check wheather triangle is possible, when sum of two sides is greater 3rd side it is perfect triangle
s1=int(input("Enter "))
s2=int(input("entr: "))
s3=int(input("Entr: "))
if s1+s2>s3 or s2+s3>s1 or s3+s1>s2 : 
    print("triangle is possible")
else:
    print("triangle is not possible")

#132.changinge variable values:
i=int(input("entr i: "))
j=int(input("entr j: "))
k=int(input("entr k: "))
if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
    if j>k:
        j=i
    else:
        i=k
print(i,j,k)

#133.Library charges per day:
nd=int(input("Entr the number of days you visited library: "))
if nd<=4:            
    print("Completely free:)")
elif nd==5:
    print(nd*2)
elif nd>=6 and nd<=10:
    print(nd*3)
elif nd>=11 and nd<=15:
    print(nd*5)
elif nd>=16 and nd<=20:
    print(nd*10)    
else:
    print("Please enter valid days upto 20")

#134.Course stream based on marks:
eg_mark=int(input("Entr english marks: "))
math_mark=int(input("Entr maths marks: "))
sci_mark=int(input("Entr science marks: "))
soc_mark=int(input("Entr Social marks: "))

if eg_mark>=80 and math_mark>=80 and sci_mark>=80 and soc_mark>=80:
    print("Congraluations You got an SCIENCE STREAM")
elif eg_mark>=80 and math_mark>=50 and sci_mark>=50:
    print("You got an COMMERCE STREAM")
elif soc_mark>=80 and eg_mark>=80:
    print("you got an HUMANITIES STREAM")
else:
    print("You got HISTRY STREAM ")

#Nested if-else Practice questions:
#135.number checker:
n=int(input("entr: "))
if n>0:
    print(f"{n} Positive")
else:
    if n<0:
        print(f"{n} Number is Negative")
    else:
        print(f"{n} Number is zero")

#136. Age classifier:
age=int(input("Ent age: "))

if age>=18 and age<=59:
    print("You are an Adult")
else:
    if age>=60:
        print("you are a senior citizen")
    else:
        print("You are an Teenager")
    
#137.Lexicographic increasing order.
x = int(input())
y = int(input())
z = int(input())
n = int(input())
coords = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
print(coords)

#138.list and tuple converter:
u=input("enter numbers: ")
li=u.split()
tu=tuple(li)
print("List: ",li)
print("tuple: ",tu)

#139.circle area calculator:
r=int(input("Enter radius: "))
x=3.14*r*r
print("The area of circle is ",x)

#140.number expansion n+nn+nnn
n=int(input())
a=int("%s" % n)
b=int("%s%s" % (n,n))
c=int("%s%s%s" % (n,n,n))
print(a+b+c)    
