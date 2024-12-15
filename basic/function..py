# passing by value
# def sum():
#     a = 10
#     b = 30
#     sum = a + b
#     print(sum)

# sum()


# passing by reference
# def sum(a,b):
#     sum = a + b
#     print(sum)

# sum(156,185)


# defaulf parameater
# def sum(a, b=4):
#     sum = a + b
#     print(sum)
#     return

# sum(15)


# return value
def sum(a,b):
    sum = a + b
    return sum

p1 = sum(15,14)
print(p1)


# multiple value using in function
# def sum(*number):
#     sum = 0
#     for num in number:
#         sum = sum + num
#     print(sum)

# sum(45,41,486,18)
