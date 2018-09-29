from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    dip_so_far, max_profit = float('Inf'), 0
    for i in range(len(prices)):
        max_profit = max(max_profit, prices[i] - dip_so_far)
        #  dip_so_far = min(dip_so_far, prices[i])
        if prices[i] < dip_so_far:  # seems faster than min approach
            dip_so_far = prices[i]
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
