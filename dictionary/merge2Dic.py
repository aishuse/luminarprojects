d={1:22,2:33,4:"hgh"}
names = {19:'Alice' ,2:'John' ,47:'Peter' ,603:'Andrew' ,6:'Ruffalo' ,15:'Chris' }
dic3=d.copy()
# dic3=names.copy()
# print(dic3)

for key,value in names.items():
    dic3[key]=value
print(dic3)


