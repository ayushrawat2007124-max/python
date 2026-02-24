str=input("enter a string :")
str=str.upper()
count=0
vowels="AEIOU"
for i in str:
    if i in vowels:
        count=count+1
print(count)       

