import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


values = [2, 3, 4, 5, 6, 7, 8, 9, 10]

deck = []

for value in values:
    for suit in suits:
        deck.append((value,suit))

num_of_games = int(input("Enter the number of games you play :- "))

player_1_win = 0
player_2_win = 0
match_draw = 0

for game in range(0,num_of_games):

    random.shuffle(deck)

    player_1 = [deck[0],deck[2],deck[4]]
    player_1.sort(key=lambda a: a[0])

    player_2 = [deck[1],deck[3],deck[5]]
    player_2.sort(key=lambda a: a[0])

    player_score = []


    for card in player_1,player_2:
        if card[0][0] == card[1][0] or card[1][0] == card[2][0]:
            if card[0][0] == card[1][0] == card[2][0]:
                player_score.append(10)
            elif card[0][0] == card[1][0]:
                player_score.append(6)
            else:
                player_score.append(6)

        elif card[0][0]+2 == card[1][0]+1 == card[2][0]:
            if(card[0][1]==card[1][1]==card[2][1]):
                player_score.append(9)
            else:
                player_score.append(8)

        elif card[0][1] == card[1][1] == card[2][1]:
            player_score.append(7)

        else:
            player_score.append(5)


    if player_score[0] > player_score[1]:
        player_1_win += 1        
    elif player_score[1] > player_score[0]:
        player_2_win += 1        
    else:
        if player_1[0][0] == player_1[1][0] == player_1[2][0] > player_2[0][0] == player_2[1][0] == player_2[2][0]:
            player_1_win += 1            

        elif player_1[0][0]+2 == player_1[1][0]+1 == player_1[2][0] > player_2[0][0]+2 == player_2[1][0]+1 == player_2[2][0]:
            if player_1[0][1] == player_1[1][1] == player_1[2][1] > player_2[0][1] == player_2[1][1] == player_2[2][1]:
                player_1_win += 1                
            else:                
                player_1_win += 1

        elif player_1[0][1] == player_1[1][1] == player_1[2][1] and player_2[0][1] == player_2[1][1] == player_2[2][1]:
            if player_1[2][0] == player_2[2][0]:
                if player_1[1][0] == player_2[1][0]:
                    if player_1[0][0] == player_2[0][0]:
                        # print("Match is draw!")
                        match_draw += 1
                    elif player_1[0][0] > player_2[0][0]:                        
                        player_1_win += 1
                    else:                        
                        player_2_win += 1
                elif player_1[1][0] > player_2[1][0]:                    
                    player_1_win += 1
                else:                    
                    player_2_win += 1
            elif player_1[2][0] > player_2[2][0]:                
                player_1_win += 1
            else:                
                player_2_win += 1

        elif (player_1[0][0] == player_1[1][0] or player_1[1][0] == player_1[2][0]) and (player_2[0][0] == player_2[1][0] or player_2[1][0] == player_2[2][0]) : 
            if player_1[1][0] == player_2[1][0]:
                p1_high = player_1[0][0] + player_1[1][0] + player_1[2][0]
                p2_high = player_2[0][0] + player_2[1][0] + player_2[2][0]
                if p1_high > p2_high:                    
                    player_1_win += 1
                else:                    
                    player_2_win += 1
            elif player_1[1][0] > player_2[1][0]:                
                player_1_win += 1
            else:                
                player_2_win += 1

        else:
            if player_1[2][0] == player_2[2][0]:
                if player_1[1][0] == player_2[1][0]:
                    if player_1[0][0] == player_2[0][0]:
                        # print("Match is draw!")
                        match_draw += 1
                    elif player_1[0][0] > player_2[0][0]:                        
                        player_1_win += 1
                    else:                        
                        player_2_win += 1
                elif player_1[1][0] > player_2[1][0]:                    
                    player_1_win += 1
                else:                    
                    player_2_win += 1
            elif player_1[2][0] > player_2[2][0]:                
                player_1_win += 1
            else:                
                player_2_win += 1

    player_score.clear()

print("Player 1 win",player_1_win)
print("Player 2 win",player_2_win)
print("Draw matches",match_draw)
print("total",player_1_win + player_2_win + match_draw)