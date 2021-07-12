n=int(input("enter a no: "))
val=n
rev=0
while(n>0):
    a=n%10
    rev=rev*10+a
    n=n//10

if(val==rev):
    print("palindrome")
else:
    print("not palindrome")