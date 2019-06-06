#!/usr/bin/python

import sys

# def helper_function():
#     pass

# plays = ["rock", "paper", "scissors"]

# def rock_paper_scissors(n):
#     if n == 0:
#         return [[]]
#     if n == 1:
#         return [["rock"], ["paper"], ["scissors"]]
#     if n > 1:
#         return helper_function(n)

# if n == 2:
#     return [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
# else:
#     c = [0 for _ in range(n)]

#     for i in range(n):
#         for j in range(0, len(plays)):
#             if c[i] == 0:
#                 c[i] = plays[j]
#             elif c[i]

#     return c


# set empty array index 0 to first element in plays

# set empty array index 1 to first element in plays

# then cycle through all three plays for index 2, saving each outcome in the
# list of lists

# then cycle to the next play in index 1

# then cycle through all plays for index 2 saving each to the list of lists

# once all combinations of index 1 and 2 are exhausted, move index 0 to the
# next play and start the process again

# repeat for the final play as


# c = [0 for _ in range(4)]
# print(c)

# print(rock_paper_scissors(2))


def rock_paper_scissors(n):

    def recursion_helper(list):
        possibilities = [['rock'], ['paper'], ['scissors']]
        new_list = []
        for item in list:
            for possibility in possibilities:
                new_list.append(item + possibility)
        return new_list

    count = 1
    answer = [['rock'], ['paper'], ['scissors']]
    if n == 0:
        return [[]]
    if n == 1:
        return answer
    while count < n:
        answer = recursion_helper(answer)
        count += 1
    return answer


print(rock_paper_scissors(2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
