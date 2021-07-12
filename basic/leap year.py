#     #  LEAP YEAR
# y=int(input("enter year: "))
# if y%4==0:
#     if (y%100==0):
#         if y%400==0:
#              print(" a leap year")
#         else:
#             print("not leap year")
#     else:
#         print("a leap year")
# else:
#     print("not at all leap year")


# for y in range(2000,2025):
#     if y%4==0:
#         if y%400==0:
#             if y%100==0:
#                 continue
#         else:
#             print(y)

s="aabbbjhjssss"

import os
import collections



a = "aaabbbgjj"
s=set(a)
print(s)
for i in s:
    print(i,a.count(i))
# for i in s:
#     sorted((a.count(i)))

