import random

A = 14
K = 13
Q = 12
J = 11

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

values = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]

# deck = []

# for value in values:
#     for suit in suits:
#         deck.append((value,suit))

deck = [(value, suit) for value in values for suit in suits]


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

    global player_1_win
    global player_2_win
    global match_draw

    trio_pl_1 = Is_trio(p1)
    trio_pl_2 = Is_trio(p2)

    if trio_pl_1 and trio_pl_2:
        if trio_pl_1 > trio_pl_2:
            player_1_win += 1
        else:
            player_2_win += 1
    elif trio_pl_1:
        player_1_win += 1
    elif trio_pl_2:
        player_2_win += 1
    else:
        ps_pl_1 = Is_pure_sequence(p1)
        ps_pl_2 = Is_pure_sequence(p2)
        if ps_pl_1 and ps_pl_2:
            if ps_pl_1 > ps_pl_2:
                player_1_win += 1
            elif ps_pl_1 < ps_pl_2:
                player_2_win += 1
            else:
                match_draw += 1
        elif ps_pl_1:
            player_1_win += 1
        elif ps_pl_2:
            player_2_win += 1
        else:
            se_pl_1 = Is_sequence(p1)
            se_pl_2 = Is_sequence(p2)
            if se_pl_1 and se_pl_2:
                if se_pl_1 > se_pl_2:
                    player_1_win += 1
                elif se_pl_1 < se_pl_2:
                    player_2_win += 1
                else:
                    match_draw += 1
            elif se_pl_1:
                player_1_win += 1
            elif se_pl_2:
                player_2_win += 1
            else:
                colour_pl_1 = Is_colour(p1)
                colour_pl_2 = Is_colour(p2)
                if colour_pl_1 and colour_pl_2:
                    if colour_pl_1[2] > colour_pl_2[2]:
                        player_1_win += 1
                    elif colour_pl_1[2] < colour_pl_2[2]:
                        player_2_win += 1
                    else:
                        if colour_pl_1[1] > colour_pl_2[1]:
                            player_1_win += 1
                        elif colour_pl_1[1] < colour_pl_2[1]:
                            player_2_win += 1
                        else:
                            if colour_pl_1[0] > colour_pl_2[0]:
                                player_1_win += 1
                            elif colour_pl_1[0] < colour_pl_2[0]:
                                player_2_win += 1
                            else:
                                match_draw += 1
                elif colour_pl_1:
                    player_1_win += 1
                elif colour_pl_2:
                    player_2_win += 1
                else:
                    double_pl_1 = Is_double(p1)
                    double_pl_2 = Is_double(p2)
                    if double_pl_1 and double_pl_2:
                        if double_pl_1[1] > double_pl_2[1]:
                            player_1_win += 1
                        elif double_pl_1[1] < double_pl_2[1]:
                            player_2_win += 1
                        else:
                            if sum(double_pl_1) > sum(double_pl_2):
                                player_1_win += 1
                            elif sum(double_pl_1) < sum(double_pl_2):
                                player_2_win += 1
                            else:
                                match_draw += 1
                    elif double_pl_1:
                        player_1_win += 1
                    elif double_pl_2:
                        player_2_win += 1
                    else:
                        high_pl_1 = Is_high_card(p1)
                        high_pl_2 = Is_high_card(p2)
                        if high_pl_1[2] > high_pl_2[2]:
                            player_1_win += 1
                        elif high_pl_1[2] < high_pl_2[2]:
                            player_2_win += 1
                        else:
                            if high_pl_1[1] > high_pl_2[1]:
                                player_1_win += 1
                            elif high_pl_1[1] < high_pl_2[1]:
                                player_2_win += 1
                            else:
                                if high_pl_1[0] > high_pl_2[0]:
                                    player_1_win += 1
                                elif high_pl_1[0] < high_pl_2[0]:
                                    player_2_win += 1
                                else:
                                    match_draw += 1


num_of_games = int(input("Enter the number of games you play :- "))

player_1_win = 0
player_2_win = 0
match_draw = 0

for game in range(0, num_of_games):
    random.shuffle(deck)

    player_1 = [deck[0],deck[2],deck[4]]
    player_1.sort(key=lambda a: a[0])

    player_2 = [deck[1],deck[3],deck[5]]
    player_2.sort(key=lambda a: a[0])

    win(p1=player_1, p2=player_2)

print("Player 1 is win ", player_1_win)
print("Player 2 is win ", player_2_win)
print("Draw matches ", match_draw)