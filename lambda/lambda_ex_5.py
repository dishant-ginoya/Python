# #   Write a function that sorts a list of dictionaries based on a complex key derived from a lambda
# #   function. Each dictionary contains a person's name, age, and salary. The sorting key should be a
# #   tuple of (age, -salary), sorting primarily by age and secondarily by salary in descending order.
# #
# #  input = people : [
# #  {"name": "Alice", "age": 30, "salary": 70000},
# #  {"name": "Bob", "age": 25, "salary": 500000},
# #  {"name": "Charlie", "age": 30, "salary": 60000}
# #  ]
# #
# #  Output :
# #  [
# #      {"name": "Bob", "age": 25, "salary": 55000},
# #      {"name": "Alice", "age": 30, "salary": 50000},
# #      {"name": "Charlie", "age": 30, "salary": 60000}
# #  ]
# # -------------------

people = [
    {"name": "Alice", "age": 30, "salary": 70000},
    {"name": "Bob", "age": 25, "salary": 500000},
    {"name": "Charlie", "age": 30, "salary": 60000}
]

output = sorted(people, key=lambda x: (x['age'], x['salary']))
print(output)