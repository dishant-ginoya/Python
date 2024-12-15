# #  You are given a list of strings. Each string represents a sentence with words separated by spaces.
# #  Write a function that processes the list and performs the following operations:
# #   a. For each sentence, convert all words to lowercase.
# #   b. Remove any words that are less than 4 characters long.
# #   c. Join the remaining words in each sentence with a hyphen - and return a list of these joined sentences.
# #
# # Input : sentences = ["The quick brown Fox jumps", "Hello world of Python", "Lambda functions are powerful"]
# # Output: ["quick-brown-fox-jumps", "hello-world-python", "lambda-functions-are-powerful" ]
# # -------------------


sentences = ["The quick brown Fox jumps", "Hello world of Python", "Lambda functions are powerful"]
print('Input :-', sentences)
print()
#
# # -------------- a. For each sentence, convert all words to lowercase --------------
#
# lower = list(map(lambda x: str(x).lower(), sentences))
# print('A :-', lower)


# # -------------- b. Remove any words that are less than 4 characters long --------------
#
# word = list(map(lambda x: ' '.join(filter(lambda word: len(word) > 4, x.split())), lower))
# print('B :-', word)


# # -------------- c. Join the remaining words in each sentence with a hyphen - and return a list of these joined sentences --------------
#
# join = list(map(lambda x: str(x).replace(' ', '-'), word))
# print('C :-', join)


output = list(map(lambda x: '-'.join(filter(lambda word: len(word) > 4, x.split())).lower(), sentences))
print('Output :-', output)
