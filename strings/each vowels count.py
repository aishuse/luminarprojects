n=input("enter a string: ")
vowels="aeiou"
def vow(n,v):
    count = 0
    for i in n:
      if i==v:
         count+=1
    return count

for i in vowels:
    c=vow(n,i)
    print(i, "=", c)
