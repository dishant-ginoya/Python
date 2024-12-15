import random

A = 14
K = 13
Q = 12
J = 11

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

values = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]

card_name_map = {14: 'Ace', 13: 'King', 12: 'Queen', 11: 'Jack'}


# deck = []

# for value in values:
#     for suit in suits:
#         deck.append((value,suit))

deck = [(value, suit) for value in values for suit in suits]

global new_line
new_line = '\n'


def Is_trio(cards):
    values = [card[0] for card in cards]
    if len(set(values)) == 1:
        return values[0]


def Is_pure_sequence(cards):
    values = [card[0] for card in cards]
    suits = [card[1] for card in cards]
    if values[0] == 2 and values[1] == 3 and values[2] == 14 and len(set(suits)) == 1:
        return values[2]
    elif values[0]+2 == values[1]+1 == values[2] and len(set(suits)) == 1:
        return values[1]


def Is_sequence(cards):
    values = [card[0] for card in cards]
    if values[0] == 2 and values[1] == 3 and values[2] == 14:
        return values[2]
    elif values[0]+2 == values[1]+1 == values[2]:
        return values[1]


def Is_colour(cards):
    values = [card[0] for card in cards]
    suits = [card[1] for card in cards]
    if (len(set(suits)) == 1):
        return values


def Is_double(cards):
    values = [card[0] for card in cards]
    if len(set(values)) == 2:
        return values


def Is_high_card(cards):
    values = [card[0] for card in cards]
    return values


def win(p1, p2):

    trio_pl_1 = Is_trio(p1)
    trio_pl_2 = Is_trio(p2)

    if trio_pl_1 and trio_pl_2:
        if trio_pl_1 > trio_pl_2:
            file.write('player 1 win \n'+ new_line)
        else:
            file.write('  player 2 win \n'+ new_line)
    elif trio_pl_1:
        file.write('player 1 win \n'+ new_line)
    elif trio_pl_2:
        file.write('  player 2 win \n'+ new_line)
    else:
        ps_pl_1 = Is_pure_sequence(p1)
        ps_pl_2 = Is_pure_sequence(p2)
        if ps_pl_1 and ps_pl_2:
            if ps_pl_1 > ps_pl_2:
                file.write('player 1 win \n'+ new_line)
            elif ps_pl_1 < ps_pl_2:
                file.write('  player 2 win \n'+ new_line)
            else:
                file.write('  Matches is Draw \n'+ new_line)
        elif ps_pl_1:
            file.write('player 1 win \n'+ new_line)
        elif ps_pl_2:
            file.write('  player 2 win \n'+ new_line)
        else:
            se_pl_1 = Is_sequence(p1)
            se_pl_2 = Is_sequence(p2)
            if se_pl_1 and se_pl_2:
                if se_pl_1 > se_pl_2:
                    file.write('player 1 win \n'+ new_line)
                elif se_pl_1 < se_pl_2:
                    file.write('  player 2 win \n'+ new_line)
                else:
                    file.write('  Matches is Draw \n'+ new_line)
            elif se_pl_1:
                file.write('player 1 win \n'+ new_line)
            elif se_pl_2:
                file.write('  player 2 win \n'+ new_line)
            else:
                colour_pl_1 = Is_colour(p1)
                colour_pl_2 = Is_colour(p2)
                if colour_pl_1 and colour_pl_2:
                    if colour_pl_1[2] > colour_pl_2[2]:
                        file.write('player 1 win \n'+ new_line)
                    elif colour_pl_1[2] < colour_pl_2[2]:
                        file.write('  player 2 win \n'+ new_line)
                    else:
                        if colour_pl_1[1] > colour_pl_2[1]:
                            file.write('player 1 win \n'+ new_line)
                        elif colour_pl_1[1] < colour_pl_2[1]:
                            file.write('  player 2 win \n'+ new_line)
                        else:
                            if colour_pl_1[0] > colour_pl_2[0]:
                                file.write('player 1 win \n'+ new_line)
                            elif colour_pl_1[0] < colour_pl_2[0]:
                                file.write('  player 2 win \n'+ new_line)
                            else:
                                file.write('  Matches is Draw \n'+ new_line)
                elif colour_pl_1:
                    file.write('player 1 win \n'+ new_line)
                elif colour_pl_2:
                    file.write('  player 2 win \n'+ new_line)
                else:
                    double_pl_1 = Is_double(p1)
                    double_pl_2 = Is_double(p2)
                    if double_pl_1 and double_pl_2:
                        if double_pl_1[1] > double_pl_2[1]:
                            file.write('player 1 win \n'+ new_line)
                        elif double_pl_1[1] < double_pl_2[1]:
                            file.write('  player 2 win \n'+ new_line)
                        else:
                            if sum(double_pl_1) > sum(double_pl_2):
                                file.write('player 1 win \n'+ new_line)
                            elif sum(double_pl_1) < sum(double_pl_2):
                                file.write('  player 2 win \n'+ new_line)
                            else:
                                file.write('  Matches is Draw \n'+ new_line)
                    elif double_pl_1:
                        file.write('player 1 win \n'+ new_line)
                    elif double_pl_2:
                        file.write('  player 2 win \n'+ new_line)
                    else:
                        high_pl_1 = Is_high_card(p1)
                        high_pl_2 = Is_high_card(p2)
                        if high_pl_1[2] > high_pl_2[2]:
                            file.write('player 1 win \n'+ new_line)
                        elif high_pl_1[2] < high_pl_2[2]:
                            file.write('  player 2 win \n'+ new_line)
                        else:
                            if high_pl_1[1] > high_pl_2[1]:
                                file.write('player 1 win \n'+ new_line)
                            elif high_pl_1[1] < high_pl_2[1]:
                                file.write('  player 2 win \n'+ new_line)
                            else:
                                if high_pl_1[0] > high_pl_2[0]:
                                    file.write('player 1 win \n'+ new_line)
                                elif high_pl_1[0] < high_pl_2[0]:
                                    file.write('  player 2 win \n'+ new_line)
                                else:
                                    file.write('  Matches is Draw \n'+ new_line)

num_of_games = int(input("Enter the number of games you play :- "))


total = 'Total Number of Matches : '+str(num_of_games)+'\n'+ new_line
file = open("teen patti results.txt", 'wt')
file.write(total)

for game in range(1, num_of_games+1):

    game_no = 'Number of Match : '+str(game)+ new_line
    file.write(game_no)

    random.shuffle(deck)

    player_1 = [deck[0],deck[2],deck[4]]
    player_1_card = '  Player 1 card : '+ ', '.join(f"({card_name_map.get(value, value)} of {suit})" for value, suit in player_1) + new_line
    file.write(player_1_card)
    player_1.sort(key=lambda a: a[0])


    player_2 = [deck[1],deck[3],deck[5]]
    player_2_card = '  Player 2 card : '+ ', '.join(f"({card_name_map.get(value, value)} of {suit})" for value, suit in player_2) + new_line
    file.write(player_2_card)
    file.write('   --> Result :')
    player_2.sort(key=lambda a: a[0])

    win(p1=player_1, p2=player_2)

file.close()

file = open("teen patti results.txt", 'rt')

player_1_win = 0
player_2_win = 0
match_draw = 0

win = []
for x in file:

    if x.count('player 1 win') == 1:
        player_1_win += 1
        win.append(1)
    if x.count('player 2 win') == 1:
        player_2_win += 1
        win.append(2)
    if x.count('Matches is Draw') == 1:
        match_draw += 1
        win.append(0)

file.close()

print('Please Check the teen patti results.txt')

print("Player 1 is win :-", win.count(1))
print("Player 2 is win :-", win.count(2))
print("Draw Matches :-", win.count(0))
print(player_1_win)
print(player_2_win)
print(match_draw)