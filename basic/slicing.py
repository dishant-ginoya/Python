# ------------------------ sliceing with string ------------------------

my_str = "Hello world!"

print(my_str)
# print(my_str[::])  #  start : end : jump  # start default 0 , end default ending , jump default 1
# print(my_str[0])
# print(my_str[2:])
# print(my_str[2:5])
# print(my_str[:2])
# print(my_str[2::2])
# print(my_str * 2)

# print(my_str[-5:-1])  # !dlrow olleh =  dlro, orld



# ------------------------ sliceing with list ------------------------

list = ["dishant", "4","viraj", "15", "parth", "mahadev", "78", "46", "karan", "abhay", "aaditya", "aasif", "22"]
list1 = [1,"a"]

# print(list[::3])  
# print(list[0:9])
# print(list[4:])
# print(list[3:10])
# print(list1 * 2)
# print(list + list1)

# var = slice(0, len(list), 2)
# print(list[var])



# ------------------------ sliceing with list ------------------------

tuple = ["dishant", "4","viraj", "15", "parth", "mahadev", "78", "46", "karan", "abhay", "aaditya", "aasif", "22"]
tuple1 = [1,"a"]

# print(tuple[::2])  
# print(tuple[0:10])
# print(tuple[1:])
# print(tuple[5:8])
# print(tuple1 * 2)
# print(tuple + tuple1)

# var = slice(0, len(tuple), 2)
# print(tuple[var])



# ------------------------ Dictionary Data type ------------------------

dict = {"Dishant":"BCA",
            "Manav":"B.Com",
            "Hitesh":"BBA",
            "Kevin": {"part-time":"std", "course":"B.Tech"}}

# dict["AAditya"]="B.Tech"
# dict.update({"abc":"xyz"})
# dict.update({"Hitesh":"xyz"})
# del  dict["Kevin"]

# d2 = dict.copy()

# print(d2)
# print(dict["Dishant"])

# print(dict.items())
# print(dict.keys())