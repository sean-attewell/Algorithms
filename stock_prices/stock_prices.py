#!/usr/bin/python

import argparse


# takes a list as input
def find_max_profit(prices):
    max_price = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i] >= max_price:
            max_price = prices[i]
            for j in range(0, i):
                if prices[j] < min_price:
                    min_price = prices[j]

    profit = max_price - min_price

    # return f"Max price ${max_price}, min price ${min_price}, profit ${profit}"
    return profit


print(find_max_profit([100, 55, 4, 98, 10, 18,
                       90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
