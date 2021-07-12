from functools import *

l=[1,2,3,4,5,6,7,8,9,10]

def even(n):
    return n%2==0
e=list(filter(even,l))
print(e)

fil=list(filter(lambda n:n%2!=0,l))
print(fil)

mapp=list(map(lambda n: n*2, fil))
print(mapp)

red=reduce(lambda a,b:a+b,mapp)
print(red)