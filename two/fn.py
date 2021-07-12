# n=int(input("enter number 1:"))
# m=int(input("enter number 2:"))
# def divisibility(n,m):
#     if n%m==0:
#         print(n, " is divisible by ", m)
#     else:
#         print(n," not divisible by ",m)
# divisibility(n,m)

#local and global variables

a=10
print("first assigned value for a : ",a)
def values():
    #print(a) #UnboundLocalError: local variable 'a' referenced before assignment
    a=9
    print("variable under values() function : ",a)
values()
def new():
    a="hello"
    print("variable under new() function : ",a)

new()
def globalvar():
    #print(a)
    global a

    print("variable under globalvar() function : ",a)
    a="changed value"
    print("variable under globalvar function after global a : ", a)
globalvar()