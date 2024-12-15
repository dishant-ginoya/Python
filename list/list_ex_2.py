# all_possibility = []

n1 = int(input('Enter First Value : - '))
n2 = int(input('Enter Second Value : - '))
n3 = int(input('Enter Third Value : - '))

sum = int(input('Enter Sum Do`t Print : -'))

# for i in range(n1+1):
#     for i in range(n1+1):
#         for k in range(n3+1):
#             if i+j+k != sum:
#                 all_possibility.append([i,j,k])

all_possibility = [[i, j, k] for i in range(n1+1) for j in range(n2+1) for k in range(n3+1) if i+j+k != sum]

print(all_possibility)
