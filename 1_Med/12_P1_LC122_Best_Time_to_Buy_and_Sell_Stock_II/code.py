# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    for _ in range(1, len(prices)):
        if prices[_] > prices[_ - 1]:
            max_profit += prices[_] - prices[_ - 1]
    return max_profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices) == 7)

prices = [1,2,3,4,5]
print(maxProfit(prices) == 4)

prices = [7,6,4,3,1]
print(maxProfit(prices) == 0)