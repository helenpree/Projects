#Checking Consonants and vowels count :
#vowels are:"aieou"
#consonants are: everything except vowels
ind=0
vowels="aieou"
user=input("Enter your word here: ")
con_count=0
vowel_count=0
while ind<len(user):
    if user[ind].lower() not in vowels and user[ind].isalpha():
        con_count+=1
    else:
        vowel_count+=1
    ind+=1
print("Consonants count are: ",con_count)
print("Vowels count are:",vowel_count)