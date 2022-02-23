'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_purchase = 0
        stocksaleprice = 0
        stock_profit = 0
        lenth = len(prices)
        if lenth == 0 or lenth == 1:
            return 0
        left, right = 0, 1
        while right < lenth:
            stock_purchase = prices[left]
            stocksaleprice = prices[right]
            if stock_purchase < stocksaleprice:
                temp_profit = stocksaleprice - stock_purchase
                stock_profit = max(temp_profit, stock_profit)
            else:
                left = right
            right += 1

        return stock_profit