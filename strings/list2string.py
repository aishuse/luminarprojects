# list=["hi","my","name"]
# s=""
# for i in list:
#     s=s+i
# print(s)
#
# def convertList(list1):
#     str = ''  # initializing the empty string
#
#     for i in list1:  # Iterating and adding the list element to the str variable
#         str+= i
#
#     return str
#
#
# list1 = ["Hello", "My", "Name is ", "Devansh"]  # passing string
# print(convertList(list1))  # Printin the converted string value


list1 = ["Hello", "My", "Name is ", "Devansh"]  # passing string
str=""
print(str.join(list1))
# print("".join(map(str,list1)))