C = 'Club'
D = 'Diamonds'
H = 'Heart'
S = 'Spade'

player_1 = [(6,D),(6,C),(8,D)]
player_1.sort(key=lambda a: a[0])

player_2 = [(4,S),(6,S),(6,H)]
player_2.sort(key=lambda a: a[0])

player_score = []

for x in player_1,player_2:
    # print(x)

    if x[0][0] == x[1][0] or x[1][0] == x[2][0]:
        if x[0][0] == x[1][0] == x[2][0]:
            # print("Is Trio")
            player_score.append(10)
        elif x[0][0] == x[1][0]:
            # print(x[0],"&",x[1],"Is double")
            player_score.append(6)
        else:
            # print(x[1],"&",x[2],"Is double")
            player_score.append(6)

    elif(x[0][0]+2 == x[1][0]+1 == x[2][0]):
        if(x[0][1]==x[1][1]==x[2][1]):
            # print("Is pure sequence")
            player_score.append(9)
        else:
            # print("Is sequence")
            player_score.append(8)

    elif(x[0][1] == x[1][1] == x[2][1]):
        # print("Is color")
        player_score.append(7)

    else:
        # print(x[2], "Is high card")
        player_score.append(5)

if player_score[0] > player_score[1]:
    print("Player 1 is win!")
elif player_score[1] > player_score[0]:
    print("Player 2 is win!")
else:
    print("Match is drow")

player_score.clear()
# print(player_score)