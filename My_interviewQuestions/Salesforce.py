'''
Write a code/function to validate the pair of parenthesis in expression. 
Return True/False


Example 
"()" → True
")(" -> False
"()())(" → False
"( ( ) ) )" -> False 
'''


# def valid_paranthesis(input):
#     if len(input) % 2 != 0:
#         return False
#
#     dict_items = {"(": 0}
#
#     for items in input:
#         if items == "(":
#             dict_items["("] += 1
#         else:
#             dict_items["("] -= 1
#             if dict_items["("] < 0:
#                 return False
#     if dict_items["("] != 0:
#         return False
#     return True
#
#
# print(valid_paranthesis("()()()"))
    
    
# 002225
#
#
# Is this a full time role
# How ofte you release
# what code are you building
# GIL
# over rite the default values in helm
# how to add list in dictionary
#
#
# GRE global release engi group

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         match = {
#                 '{': '}',
#                 '(': ')',
#                 '[': ']'
#             }
#         for i in s:
#             if i in match:
#                 stack.append(match[i])
#             elif stack and stack[-1] == i:
#                 stack.pop()
#             else:
#                 return False
#         return stack == []
#
# result = Solution()
# result.isValid("[][]")



### Sorted word count

# Assume that words.txt has the following content:
# the day is sunny the the the
# sunny is is
#
# Your script should output the following, sorted by descending frequency:
# the 4
# is 3
# sunny 2
# day 1

def Sorted_words():
   Words_dict = {}
   with open('words.txt', 'r') as f:
      for line in f:
          for word in  line.split(" "):
            word = word.strip('\n')
            if word not in Words_dict:
                Words_dict[word] = 0
            Words_dict[word] += 1
 #  return(Words_dict)

   Count_list = []
   for word, count in Words_dict.items():
      Count_list.append((count, word))
   Count_list = Count_list.sort()#sorted(Count_list, reverse=True)
   return(Count_list)


print(Sorted_words())
# [‘the’, ’ is ’]
# [4, 3]
# [(4,’the’), (3, ‘ is ’)]









