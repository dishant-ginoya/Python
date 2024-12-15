# --------------- local variable ---------------

a = b = 100

print(a)
print(b)

name,age = "Dishant", 21

print(name)
print(age)

counter = 100
_count  = 10
name1 = "Dishant"
name2 = "Ginoya"
Age  = 21

del _count

# print (counter)
# print (_count)
# print (name1)
# print (name2)
# print (Age)


def sum(x,y):
   sum = x + y
   return sum
# print(sum(5, 10))


# --------------- global variable ---------------

x = 5  # Global
y = 10

def myfunc():
  x = 3
  y = 7  # Local
  print(x + y)  # Local Variable

myfunc()

print(x + y)  # Global Variable 