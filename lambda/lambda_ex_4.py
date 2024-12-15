# #   Filtering and Transforming
# #   Write a function that filters a list of strings to include only those that contain a given substring,
# #   and then transforms each remaining string by applying a lambda function that reverses the string
# #
# # strings = ["hello", "world", "hell", "welcome"]
# # Input: substring = "hell"
# # Output : ['olleh', 'lleh']
# # -------------------


strings = ["hello", "world", "hell", "welcome"]
substring = "hell"
#
output = list(filter(lambda x: (substring in x) ,strings))
print(list(map(lambda x:x[::-1],output)))
print(output)


