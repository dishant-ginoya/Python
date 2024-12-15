dict = {"Dishant":"BCA",
            "Manav":"B.Com",
            "Hitesh":"BBA",
            "Kevin": {"part-time":"std", "course":"B.Tech"}}

dict_ = {"BA":"30000", "B.Com":"25000", "BBA":"29000"}

# x = {1:{'a':15},3:{'a':14},2:{'a':17}}
# a = dict(sorted(dict_.items(), key=lambda item: item[1]))
# b = dict(sorted(x.items(), key=lambda x:x[1]['a'], reverse=True))
# print(a)

# print(dict)

# print(type(dict))

#   print value of key
# print(dict["Dishant"])

#  updating dictionary 
# dict["AAditya"]="B.Tech"  #  if key is not in dictiory then otherwise key of value updating
# dict["Dishant"] = "MCA"
# print(dict)

# Delete particular key & value
# del dict['Manav']
# print(dict)


# del dict
# print(dict)


# clear a dictionary
# dict.clear()
# print(dict)


#  length
# print(len(dict))

#  copy a dictionary

# dict_ = dict.copy()
# print(dict_)


#  item , keys and values
# print(dict.items()) #  all dictionary
# print(dict.keys())
# print(dict.values())


#   extend other dictionary
# dict.update(dict_)
# print(dict)


#   Get value of key
# print(dict.get("Dishant"))


#   creting a new dictionary form list & tuple
# seq = ['name', 'age']
# new = dict.fromkeys(seq)
# new = dict.fromkeys(seq,10)  # 10 is value for all element
# print(new)


for x,y in dict_.items():
    print(x,y)