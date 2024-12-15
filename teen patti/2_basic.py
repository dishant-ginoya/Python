# list = [5, 7, 4]
C = 'Club'
D = 'Diamonds'
H = 'Heart'
S = 'Spade'

list = [(5,S),(7,H),(5,C)]
list.sort()
# print(list)

#  three element

if list[0][0] == list[1][0] == list[2][0]:
    print("All elemnet is equal")
elif list[0][0] == list[1][0]:
    print(list[0],list[1],"is two element is same")
elif list[1][0] == list[2][0]:
    print(list[1],list[1],"is two element is same")
else:
    print("All element is not equal")




# sequence 

# if(list[0]+1 == list[1] and list[1]+1 == list[2]):
#     print("the is a sequence")
# else:
    # print("not sequence")



#  color

# if(list[0][1]==list[1][1]==list[2][1]):
#     print("Is color")


# pure sequence

# if(list[0][1]==list[1][1]==list[2][1] and list[0][0]+1 == list[1][0] and list[1][0]+1 == list[2][0]):
#     print("Is pure sequence")



#   higt card

# print(list[2], "Is high card")


