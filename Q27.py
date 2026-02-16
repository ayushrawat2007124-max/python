n=int(input("enter a number"))
temp=0
rev=0
store=n
while(n!=0):
    temp=n%10
    rev=((rev*10)+temp)
    n=n//10
if(store==rev):
    print("Number is a palindrome number",store)
else:
    print("Number is not a palindrome  number",store)        