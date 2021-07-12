color = ['Red', 'Green', 'Black']
print("Original List: ",color)
color = [v for i in color for v in ('c', i)]
print("Original List: ",color)



colors = [['Red'], ['Green'], ['Black']]
for i in colors:
    print(i)