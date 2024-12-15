# # ---------------- 1. Invert a Dictionary ----------------
#
# number = int(input('Enter how many key-value pair add :- '))
# result = {}
#
# for i in range(number):
#     print()
#     key = input('Enter new key :- ').strip()
#     value = input(f'Enter {key} value :- ').strip()
#     if key and value:
#         result.update({
#             key:int(value)
#         })
#
# output = {i: [j for j in result if result[j] == i] for i in result.values()}
# print(output)
#
# # - - - - - - - - - -
# # output : {1: ['a', 'c'], 2: ['b']}




# # ---------------- 2. Merge Dictionaries ----------------
#
# dict_1 = {'a': 1, 'b': 2}
# dict_2 = {'b': 3, 'c': 4}
#
# result ={}
# [result.update({d1: result[d1]+dict_1[d1]}) if d1 in result else result.update({d1: dict_1[d1]}) for d1 in dict_1]
# [result.update({d2: result[d2]+dict_2[d2]}) if d2 in result else result.update({d2: dict_2[d2]}) for d2 in dict_2]
#
# print(result)
#
# # - - - - - - - - - -
# # input : dict_1 : {'a': 1, 'b': 2}
# # dict_2 : {'b': 3, 'c': 4}
# # output : {'a': 1, 'b': 5, 'c': 4}




# # ---------------- 3. Top K Frequent Elements ----------------
#
# top_freq_number = int(input('Enter number you want to top frequent elements :- '))
# number_list = list(map(int, input('Enter number separate by space : ').split()))
#
# output = {number: number_list.count(number) for number in set(number_list)}
# output = dict(sorted(output.items(), key=lambda x: x[1], reverse=True))
#
# result = []
# [result.append(i) for i in output if len(result) < 2]
# print(result)
#
# # - - - - - - - - - -
# # input : [1, 1, 1, 2, 2, 3]
# # k = 2
# # output : [1, 2]




# # ---------------- 4. Dictionary From Lists ----------------
#
# list_1 = list(input('Enter List 1 value : ').split())
# list_2 = list(input('Enter List 2 value : ').split())
#
# output = {list_1[i]: list_2[i] for i in range(len(list_1))} if len(list_1) == len(list_2) else 'Please Enter equal length of list'
#
# print(output)
# # - - - - - - - - - -
# # input : ['a', 'b', 'c'], [1, 2, 3]
# # output : {'a': 1, 'b': 2, 'c': 3}




# # ---------------- 5. ----------------
#
# input = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
#
# sorted_key = {}
# [sorted_key[''.join(sorted(i))].append(i) if ''.join(sorted(i)) in sorted_key else sorted_key.update({''.join(sorted(i)): [i]}) for i in input]
#
# print(sorted_key)
# # - - - - - - - - - -
# # input : ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# # output : {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}




# # ---------------- 6. Count Letters ----------------
#
# input = input('Enter String :- ')
#
# output = {i: int(input.count(i)) for i in set(input)}
#
# print(output)
#
# # - - - - - - - - - -
# # input : "abracadabra"
# # output : {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}




# # ---------------- 7. Dictionary Comprehension ----------------
#
# number_list = list(map(int, input('Enter number separate by space : ')))
#
# output = {i: i*i for i in number_list if i % 2 == 0}
#
# print(output)
#
# # - - - - - - - - - -
# # input : [1, 2, 3, 4, 5]
# # output : {2: 4, 4: 16}




# # ---------------- 8. Count Word Occurrences ----------------
#
# intput = ["this is a test", "this is another test", "test the function"]
# # new_string = [j for i in intput for j in i.split()]
# output = {word: [j for i in intput for j in i.split()].count(word) for word in set([j for i in intput for j in i.split()])}
#
# print(output)
#
# # - - - - - - - - - -
# # intput : ["this is a test", "this is another test", "test the function"]
# # output : {'this': 2, 'is': 2, 'a': 1, 'test': 3, 'another': 1, 'the': 1, 'function': 1}




# # ---------------- 9. Nested Dictionary Merge ----------------
#
# dict_1 = {'a': {'x': 1}, 'b': {'y': 2}}
# dict_2 = {'a': {'z': 3}, 'b': {'y': 4}, 'c': {'w': 5}}
#
# result = {}
# [result.update({d1: {**result[d1],**dict_1[d1]}}) if d1 in result else result.update({d1: dict_1[d1]}) for d1 in dict_1]
# [result.update({d2: {**result[d2],**dict_2[d2]}}) if d2 in result else result.update({d2: dict_2[d2]}) for d2 in dict_2]
#
# print(result)
#
# # - - - - - - - - - -
# # input : d1 = {'a': {'x': 1}, 'b': {'y': 2}}
# #         d2 = {'a': {'z': 3}, 'b': {'y': 4}, 'c': {'w': 5}}
# # output : {'a': {'x': 1, 'z': 3}, 'b': {'y': 4}, 'c': {'w': 5}}




# # ---------------- 10. Count Number In List ----------------
#
# number_list = list(map(int, input('Enter number separate by space : ').split()))
#
# output = {number: number_list.count(number) for number in set(number_list)}
# print(output)
#
# # - - - - - - - - - -
# # input : [1, 2, 2, 3, 3, 3, 4]
# # output : {1: 1, 2: 2, 3: 3, 4: 1}
