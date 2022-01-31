'''
Problem Statement
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.
Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

# class Solution():
#     def FruitsinBasket(self, Fruit):
#         dist_Fruits = set()
#         count = 0
#         Max_sum = Sum = 0
#         i = j = 0
#         if len(Fruit) < 2: return 0
#         while j < len(Fruit):
#             if Fruit[j] in dist_Fruits:
#                 Sum += 1
#             elif count < 2:
#                  count += 1
#                  dist_Fruits.add(Fruit[j])
#                  Sum += 1
#             else:
#                 j = i
#                 i += 1
#                 Sum = count = 0
#                 dist_Fruits = set()
#             j += 1
#             if Sum > Max_sum: Max_sum = Sum
#         return Max_sum
from collections import defaultdict


# class Solution():
#     def FruitsinBasket(self, Fruit):
#         dist_Fruits = {}#defaultdict(int)
#         count = 0
#         Max_sum = Sum = 0
#         left = right = 0
#         for right, f in enumerate(Fruit):
#             #print(f)
#             if f not in dist_Fruits:
#                 dist_Fruits[f] = 1
#             else:
#                 dist_Fruits[f] += 1
#             while len(dist_Fruits) > 2:
#                 dist_Fruits[Fruit[left]] -= 1
#                 if dist_Fruits[Fruit[left]] == 0:
#                     del dist_Fruits[Fruit[left]]
#                 left += 1
#             Max_sum = max(Max_sum, right - left + 1)
#         return Max_sum


s = Solution()
#print(s.FruitsinBasket(['A', 'B', 'C', 'A', 'C']))
print(s.FruitsinBasket(['A', 'B', 'C', 'A', 'A', 'C', 'C', 'C','B', 'C', 'C', 'C']))
# print(s.FruitsinBasket(['A']))



'''
Timecomplexity = O(n2)
SpaceComplexity = O(1)
'''