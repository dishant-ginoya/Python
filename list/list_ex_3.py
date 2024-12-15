# result = []

number = int(input('Enter Number Entry You want to add :- '))
result = [(input('Enter Student Name :- '), float(input('Enter Student Grade :- '))) for i in range(number)]

# for i in range(number):
#     print()
#     name = input('Enter Student Name :- ')
#     mark = float(input('Enter Student Grade :- '))
#     result.append((name, mark))

lowest_grade = result[0][1]
second_lowest_grade = float('inf')

for grade in result:
    if grade[1] < lowest_grade:
        second_lowest_grade, lowest_grade = lowest_grade, grade[1]
    elif grade[1] < second_lowest_grade and grade[1] > lowest_grade:
        second_lowest_grade = grade[1]


print('\nStudent Name Is : - ', end='')
for name in result:
    if second_lowest_grade == name[1]:
        print(name[0],end=', ')