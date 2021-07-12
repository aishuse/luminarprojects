# class Computer:
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#     def config(self):
#         print("configuration is : ",self.cpu,self.ram)
#     def hai(self):
#         print(self.ram)
# com1=Computer("cpu 5",15)
# com2=Computer("cpu 25",55)
# com1.config()
# com2.config()
# com2.hai()



class Computer:
    def __init__(self):
        self.name='navin'
        self.age=28
    def update(self):
        self.age=30
c1=Computer()
c2=Computer()

print(c1.name)
print(c1.age)


print(c2.name)
print(c2.age)

c1.update()
print(c1.age)

# c2.update()
# print(c2.age)

