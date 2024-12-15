# #  You are given a list of tuples where each tuple contains a person's
# #  name and age. Write a function that sorts this list by age using a
# #  lambda function as the key in the sort operation.
# #
# # Output: [("Bob", 25), ("Alice", 30), ("Charlie", 35)]
# # -------------------


people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

output = list(sorted(people, key=lambda x: x[1]))
print(output)
