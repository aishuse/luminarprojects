index = [1, 2, 3]
languages = ['python', 'c', 'c++','dfgh']

d={i:j for i,j in zip(index,languages)}                 #list comprehension
print(d)

d=dict(zip(languages,index))
print(d)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_dict = {i: i**2 for i in list1}
print(square_dict)

x=dict(zip(list1,list1))
print(x)

def Convert_dict(a):
    init = iter(list1)
    res_dct = dict(zip(init, init))
    return res_dct


# Driver code
list1 = ['x', 1, 'y', 2, 'z', 3]
print(Convert_dict(list1))