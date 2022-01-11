'''
Write a code/function to validate the pair of parenthesis in expression. 
Return True/False


Example 
"()" → True
")(" -> False
"()())(" → False
"( ( ) ) )" -> False 
'''


def valid_paranthesis(input):
    if len(input) % 2 != 0:
        return False
        
    dict_items = {"(": 0}
    
    for items in input:
        if items == "(":
            dict_items["("] += 1
        else:
            dict_items["("] -= 1
            if dict_items["("] < 0:
                return False
    if dict_items["("] != 0:
        return False
    return True


print(valid_paranthesis("()()()"))
    
    
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