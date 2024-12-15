set1 = {('a',1),('b',2),('c',3),('a',100)}
set2 = {('a',45),('b',5),('d',6),('a',44)}



# # ----- multiple vlaue in tuple ------
# comman = dict(set1).keys() & dict(set2).keys()
#
# output = {(i,(dict(set1)[i],dict(set2)[i])) for i in comman}
#
# print(output)
# # output = {('b', (2, 5)), ('a', (1, 45))}


# output = set()
# key = dict(set1).keys() & dict(set2).keys()
# for i in key:
#     output.add((i[0],(dict(set1)[i[0]],dict(set2)[i[0]])))
#
# print(output)





# # ----- 1.) two vlaue in tuple ------

# output = [(i,(j,dict(set2)[i])) for i,j in dict(set1).items() if i in dict(set2)]

# print(set(output))





# # ----- 2.) two vlaue in tuple ------
# output = set()
# for i,j in dict(set1).items():
#     if i in dict(set2):
#         output.add((i,(j,dict(set2)[i])))
# print(output)





# # ----- 3.) two vlaue in tuple ------
# o = {}

# for i in set1.union(set2):
#     if i[0] in o:
#         if len(o[i[0]]) < 2:
#             o[i[0]].append(i[1])
#     else:
#         o[i[0]] = [i[1]]
# # print(o)


# output = set()
# for i,j in o.items():
#     if len(j) > 1:
#         output.add((i,tuple(set(j))))

# print(output)






# # ----- multiple vlaue in tuple ------
#
# dict = {i[0]: [a[1] for a in set1.union(set2) if i[0]==a[0]] for i in set1.union(set2)}

# output = {(i,tuple(j)) for i,j in dict.items() if len(j) > 1}

# print(output)



# # Abhishek ----- multiple vlaue in tuple ------
# re = {}
# ans=[(i[0],(i[1],j[1])) for i in set1 for j in set2 if i[0]==j[0]]


# for i in ans:
#     if i[0] in re:
#         re[i[0]] = tuple(set(list(re[i[0]])+list(i[1])))
#     else:
#         re[i[0]] = (i[1])



# output = [(i,(j)) for i,j in re.items()]

# print(set(output))


 
# # Hensi  ----- multiple vlaue in tuple ------
# def intersections(s1,s2):
#     l1 = []
#     di = {}
#     for i in s1:
#         for j in s2:
#             if i[0] == j[0]:
#                 l1.append((i[0],(i[1],j[1])))
#     for k in l1:
#         if k[0] in di:
#             di[k[0]] = tuple(set(list(di[k[0]])+list(k[1])))
#         else:
#             di[k[0]] = (k[1])
#
#     return set([(i,(j)) for i,j in di.items()])
#
# a1 = {('a',1),('b',2),('c',3)}
# b2 = {('a',4),('b',5),('d',6), ('a',44)}

# print(intersections(set1,set2))


