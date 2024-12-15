# tuple1 = (1, 2, 3)
# tuple2 = ('a', 'b', 'c')
# Output: (1, 'a', 2, 'b', 3, 'c')

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
# output = []

output = [(tuple1[i],tuple2[i]) for i in range(len(tuple1))]
# for i in range(len(tuple1)):
#      output.append(tuple1[i])
#      output.append(tuple2[i])

print(tuple(output))


# test_list1 = (1, 4, 5)
# test_list2 = (3, 8, 9)
# test_list3 = (30, 80, 90)
#
# res = list(test_list1 + test_list2 + test_list3)
#
# res[::3] = test_list1
# res[1::3] = test_list2
# res[2::3] = test_list3
#
# print("The interleaved list is : ", tuple(res))

# text = "Zfill Example"
# # Calling Function
# str2 = text.fill(30)
# # Displaying result
# print(str2)