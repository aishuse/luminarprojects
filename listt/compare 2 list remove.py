list=["qwerty","asdfg","zxcvb"]
list2=["dfgh","qwerty","asdfkjg","zxcvb"]
if list==list2:
    print("same")
else:
    print("not same")

list.remove("qwerty")
print(list)
list2.pop()
print(list2)