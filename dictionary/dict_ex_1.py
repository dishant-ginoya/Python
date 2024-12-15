students = {
    'Alice': 'A',
    'Bob': 'B',
    'Charlie': 'A',
    'David': 'C',
    'Eve': 'B'
}



# # ------------- 1. --------------
#
# result = {i:[j for j in students if students[j]==i] for i in students.values()}
#
# print(result)



# # ------------- 2. creating dict --------------
#
# dict = {}
# for i in range(1,5+1):
#     dict[i] = 'value_{}'.format(i)
#
# print(dict)



# # ------------- 3. Accessing value in dict --------------
#
# input = input('Which student find grade ? :- ').capitalize().strip()
# if students.get(input):
#     print(input, 'value is', students[input])
# else:
#     print(f'Opps, {input} is not found in dict...')



# # ------------- 4. Adding and updating iteams in dict --------------
#
# name = input('Enter new student name :- ').capitalize().strip()
# grade = input('Enter student garde :- ').upper().strip()
#
# if name and grade:
#     students[name] = grade
#
# print(students)



# # ------------- 5. Removing iteams in dict --------------

# name = input('Enter new student name :- ').capitalize().strip()
# if name:
#     del students[name]
#     grade = students.pop(name)
#     print(f'{name}`s grade is {grade}')
#
# items = students.popitem()
# print(f'{items[0]}`s grade is {items[1]}')
#
# print(students)



# # ------------- 6. dict. methods --------------
#
# print(students.keys())
# print(students.values())
# print(students.items())



# # ------------- 7. looping method in dict. --------------
#
# for name in students.keys():
#     print(name)
#
# for grade in students.values():
#     print(grade)
#
# for name,grade in students.items():
#     print(f'{name}`s grade is {grade}')



# # ------------- 8. dict. comprehensions --------------
#
# dict = {i.lower():j.lower() for i,j in students.items()}
# print(dict)



# # ------------- 9. nested dict. --------------
#
# nested_dict = {}
#
# number = int(input('How many student mark and grade add? :- '))
# for i in range(number):
#     print()
#     name = input('Enter student name :-').capitalize().strip()
#     mark = input('Enter student mark :-').strip()
#     grade = input('Enter student grade :-').capitalize().strip()
#     # student.update({
#     #     'Mark':mark,
#     #     'Grade':grade
#     # })
#
#     nested_dict.update({
#         name:{
#             'Mark': int(mark),
#              'Grade': grade
#         }
#     })
#
# print(nested_dict)



# # ------------- 10. common errors and exceptions in dict. --------------
#
# input = input('Which student find grade ? :- ').capitalize().strip()
# # if students.get(input):
# #     print(input, '`s Grade` is', students[input])
# # else:
# #     print(f'Opps, {input} is not found in dict...')
#
# try:
#     print(input, '`s Grade` is', students[input])
# except:
#     print(f'Opps, {input} is not found in dict...')

