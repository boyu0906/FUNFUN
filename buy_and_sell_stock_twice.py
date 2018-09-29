from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    max_profit, dip_so_far = 0, float('inf')
    forward_profit = [0] * len(prices)
    # backward_profit = [0] * len(prices)
    for i in range(len(prices)):
        max_profit = max(max_profit, prices[i] - dip_so_far)
        forward_profit[i] = max_profit
        dip_so_far = min(dip_so_far, prices[i])

    peak_so_far = float('-inf')
    for i in reversed(range(1, len(prices))):
        max_profit = max(max_profit, peak_so_far - prices[i] + forward_profit[i-1])
        peak_so_far = max(peak_so_far, prices[i])

    # max_profit = forward_profit[len(prices)-1]
    # for i in range(len(prices)-1):
    #     max_profit = max(max_profit, forward_profit[i] + backward_profit[i+1])

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
