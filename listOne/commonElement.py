def fun(list1,list2):
    for i in list1:
        if i in list2:
            print(i)
            return True
print(fun([11,2,4,3],[1,4,5]))

print(fun(["ab","nm","kl","io"],["qw","er","tg","ab"]))

l= ["ab","nm","kl","io"]
m= ["qw","er","tg","ab"]
print(set(l) & set(m))

j=[11,2,4,3]
k=[1,4,5]
print(set(j) & set(k))