import random as r

# choice in tuple , list & dict

list = [1,2,3,4,5,6]
print(r.choice(list))
print(r.choice('A string')) # A String is A-z
# print()


# randomly selected element from range

# print(r.randrange(100,1000,2)) #  start , end , jump  # start default 0 , end default ending , jump default 1
 # even number give 

# print(r.randrange(1,15,3)) # 1, 4, 7, 10, 13
# print()


# random 
# print(r.random)
# print()


# seed 
# print(r.seed(10))
# print(r.seed(15))
# print()


# shuffle  only list  
# list = [1,2,3,4,5,6]
# r.shuffle(list)
# print(list)
# print()


# uniform (Random Float value between x & y) 
# print(r.uniform(10,15))
# print(r.uniform(30,50))