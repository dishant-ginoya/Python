# string = 'banana'
#
# # # all substrings list create
# all_substrings = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1) if
#                   len(string[i:j]) > 1]
#
# # all_substrings = []
# # for i in range(len(string)):
# #     for j in range(i + 1, len(string) + 1):
# #         substring = string[i:j]
# #         if len(substring) > 1:
# #             all_substrings.append(substring)
# # print(all_substrings)
#
#
# # # all substrings count
# substrings_count = {substring: all_substrings.count(substring) for substring in set(all_substrings)}
#
# # substrings_count = {}
# # for substring in set(all_substrings):
# #     # substrings_count.update({
# #     #     substring: all_substrings.count(substring)
# #     # })
# #     substrings_count[substring] = all_substrings.count(substring)
# # print(substrings_count)
#
#
# # # all substrings count in des. order first pro. is len of value and after len of key
# longest_substrings = dict(sorted(substrings_count.items(), key=lambda x: (x[1], len(x[0])), reverse=True))
# # print(longest_substrings)
#
#
# # # ------- Check this value for output 'test case' ----
# # longest_substrings = {'ana': 2, 'afn': 2, 'naj': 1, 'banana': 1, 'banan': 1, 'anana': 1, 'bana': 1, 'anan': 1, 'nana': 1, 'ban': 1, 'nan': 1, 'ba': 1}
#
#
# # # counting substrings are append final list
# output = []
# [output.append(i) for i in longest_substrings if
#  not output or (longest_substrings[i] == longest_substrings[output[0]] and len(i) == len(output[0]))]
#
# # for i in longest_substrings:
# #     if not output:
# #         output.append(i)
# #     else:
# #         if longest_substrings[i] == longest_substrings[output[0]]:
# #             if len(i) == len(output[0]):
# #                 output.append(i)FFFff
#
# print(output)




# def person_lister(f):
#     def inner(people):
#         people_sorted = sorted(people, key=lambda x: int(x[2]))
#
#         return [f(person) for person in people_sorted]
#
#
#     return inner
#
# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
#
# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print(*name_format(people), sep='\n')
