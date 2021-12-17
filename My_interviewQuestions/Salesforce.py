Monday, December 6th
Interview Schedule:
https://appleinc.webex.com/appleinc/j.php?MTID=m8c0d35e67f50ea87801bb099162b63b6
Host Key: 231482
Coderpad Link - https://app.coderpad.io/ZKMTHTCD
2:30 p.m. to 2:45 p.m. PST with Connie Bustillo
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
        
    dict_items = {"(":0}
    
    for items in input:
        if items == "(":
            dict_items["("] += 1
        elif  dict_items["("] <= 0:
            return False
        else:
            items["("] -= 1
    if dict_items["("] != 0:
        return False
    return True


        
    
    
002225


Is this a full time role 
How ofte you release
what code are you building
GIL
over rite the default values in helm
how to add list in dictionary


GRE global release engi group





