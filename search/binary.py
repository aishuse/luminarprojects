def binary(lst,n):
    l = 0
    u = len(lst) - 1
    global mid
    while l<=u:
        mid=(l+u)//2
        print(mid)
        if n==lst[mid]:
            return mid
        elif n<lst[mid]:
            u=mid-1
        else:
            l=mid+1
    return False
lst=[1,2,35,11,4,3,8,9]
x=sorted(lst)
print(x)
n=11

if binary(x,n):
    print("found index",mid)
else:
    print("not")


