# while True:
#     try:
#         match = int(input('How Many Team Played :- '))
#         print()
#         break
#     except ValueError as e:
#         print(' ---- Please Enter Digit ----\n')
#
# runner_up = []
#
# for i in range(1, match+1):
#     while True:
#         try:
#             match_score = int(input('Please Enter ' + str(i) + ' Team Score :- '))
#             runner_up.append(match_score)
#             break
#         except ValueError as e:
#             print(' ---- Please Enter Digit ----\n')
#
#
# print('\nAll Team Score is - ', end='')
# for i in runner_up:
#     print(i,end='  ')
#
# high_score = max(runner_up)
# runner_up_score = set(runner_up)
# runner_up_score.remove(high_score)
#
# print('\nRunner Up Team`s Scored is', max(runner_up_score))

if __name__ == '__main__':
    n = int(input())
    arr = map(float, input().split())
    list_arr = list(arr)
    winner = list_arr[0]
    runner_up = float('inf')
    for val in list_arr:
        if val < winner:
            runner_up, winner = winner, val
        elif val < runner_up and val > winner:
            runner_up = val
    if runner_up == float('inf'):
        runner_up = None
    print(runner_up)


