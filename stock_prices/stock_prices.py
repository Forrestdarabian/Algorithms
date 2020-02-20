#!/usr/bin/python

import argparse


def find_max_profit(prices):
    minPrice = prices[0]
    maxPrice = prices[1]
    profit = maxPrice - minPrice
    for val in prices[2:]:
        newProfit = val - minPrice
        if newProfit > profit:
            print('profit', newProfit)
            profit = newProfit
        if val < minPrice:
            print('min', val)
            minPrice = val

    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
