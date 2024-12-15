# #   class simple
# class Emp():
#     name =  'Dishant'
#     def info(self):
#         print("Hii", self.name)

# emp = Emp()
# # emp.name = "abc"
# emp.info()


# #   constructor 
# class person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def Show(self):
#         print(f'\nHii {name} \nYour Age is {age}')


# name = input(str('Enter your name :- ')).capitalize()
# age = input(str('Enter your age :- '))

# p = person(name, age)
# p.Show()





#   inheritance 
class A():
    def name(self):
        name  = str(input('Enter your name :- ')).capitalize()
        self.name = name

class B(A):
    def Show(self):
        print("Hiii,", self.name)


b = B()
b.name()
b.Show()
