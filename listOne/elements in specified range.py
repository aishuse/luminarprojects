def fun(l,x,y):
    # x=4
    # y=9
    ctr=0
    for i in l:
        if i>=x and i<=y:
            # print(i)

            ctr+=1
    return ctr


l=[1,2,3,4,5,67,8,9,10]
print(fun(l,5,9))

li=['a','b','c','d','e','f']
print(fun(li,"a","b"))