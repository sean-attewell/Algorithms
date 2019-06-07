#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


# def eating_cookies(n, cache=None):
#     if n >= 2:
#         ways = 0
#         eat_at_a_time = [1, 2, 3]
#         for i in range(0, len(eat_at_a_time)):
#             if n // eat_at_a_time[i] > 0:
#                 ways += 1
#                 eating_cookies(i[n])
#     else:
#         ways = 1
#         return ways

# http://www.pythontutor.com/visualize.html#mode=display


# works for small
# def eating_cookies(n):
#     if n < 0:
#         return 0
#     elif n == 0 or n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         ans = eating_cookies(
#             n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
#         return ans


# This solution works on large too if you convert the test to object instead of arrays
def eating_cookies(n, cache={}):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    elif str(n) in cache:
        return cache[str(n)]
    else:
        cache[str(n)] = eating_cookies(
            n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        return cache[str(n)]


# TO TELL WHERE YOU ARE IN PYTHONTUTOR:

# def eating_cookies(n, place=0):
#     print(place)
# 	  if n < 0:
#         return 0
#     elif n == 0 or n == 1:
# 	      return 1
#     elif n == 2:
#         return 2
# 	  else:
# 	      ans = eating_cookies(
# 	            n - 1, 1) + eating_cookies(n - 2, 2) + eating_cookies(n - 3, 3)
# 	       return ans

# 	eating_cookies(4)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
