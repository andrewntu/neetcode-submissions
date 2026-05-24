class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while l < r and r < len(prices):
            if prices[r] > prices[l]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return res

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = prices[0]
#         res = 0

#         for i, price in enumerate(prices):
#             if price < min_price:
#                 min_price = price

#             profit = price - min_price
#             res = max(res, profit)

#         return res