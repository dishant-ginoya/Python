C = 'Club'
D = 'Diamonds'
H = 'Heart'
S = 'Spade'

player_1 = [(6,D),(6,C),(8,D)]
player_1.sort(key=lambda a: a[0])


if player_1[0][0] == player_1[1][0] or player_1[1][0] == player_1[2][0]:
    if player_1[0][0] == player_1[1][0] == player_1[2][0]:
        print("Is Trio")
    elif player_1[0][0] == player_1[1][0]:
      print(player_1[0],"&",player_1[1],"Is double")
    else:
        print(player_1[1],"&",player_1[2],"Is double")

elif(player_1[0][0]+2 == player_1[1][0]+1 == player_1[2][0]):
    if(player_1[0][1]==player_1[1][1]==player_1[2][1]):
        print("Is pure sequence")
    else:
        print("Is sequence")

elif(player_1[0][1] == player_1[1][1] == player_1[2][1]):
    print("Is color")

else:
    print(player_1[2], "Is high card")

# elif player_1[0][0] == player_1[1][0]:
#     print(player_1[0],"&",player_1[1],"Is double")
# elif player_1[1][0] == player_1[2][0]:
#     print(player_1[1],"&",player_1[2],"Is double")