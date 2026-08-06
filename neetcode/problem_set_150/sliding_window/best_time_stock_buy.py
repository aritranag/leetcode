def maxProfitBrute(prices : list[int]) -> int:
    max_profit = 0
    for i in range(len(prices) - 1):
        buy_price = prices[i]
        sell_price = max(prices[i+1:])
        profit = sell_price - buy_price
        max_profit = max(profit, max_profit)

    return max_profit

def maxProfit2Pointer(prices : list[int]) -> int:
    max_profit = 0
    l,r = 0,1
    while r < len(prices):
        if prices[l] < prices[r]:
            max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
        else:
            l = r
            r = l+1

    return max_profit

def maxProfitDp(prices : list[int]) -> int:
    max_profit = 0
    minBuy = prices[0]

    for sell_price in prices:
        max_profit = max(max_profit, sell_price - minBuy)
        minBuy = min(minBuy, sell_price)

    return max_profit

prices = [10,1,5,6,7,1]
print(maxProfitDp(prices))