x=int(input("enter a num: "))
y=int(input("enter a num: "))
if x>y:
    small=y
else:
    small=x
hcf=0
while(True):
    if x%small==0 and y%small==0:
        hcf=small
        break

    small-=1
print(hcf)

# for i in range(0,small+1):
#     if x%i==0 and y%i==0:
#         hcf=i
#         # break
# print(hcf)