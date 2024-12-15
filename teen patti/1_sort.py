C = 'Club'
D = 'Diamonds'
H = 'Heart'
S = 'Spade'

player_1 = [(6,D),(6,C),(8,D)]
player_1.sort(key=lambda a: a[0])

print(player_1)


player_2 = [(4,S),(6,S),(6,H)]
player_2.sort(key=lambda a: a[0])
print(player_2)