#Find the index in an array of ints where the difference between sum on the left and the sum on the right is minimal.
#
#Example:
#
#[ 2, 3, 8, 1] ## answer is 2 -- 2 + 3 = 5, 8 +1 =9 


def min_index(input):
    if len(input) == 0:
        return 0
    if len(input) == 1:
        return 1
        
    result = {}
    
    for index in range(len(input)):
        left_list = input[:index]
        right_list = input[index:]
        
        difference = abs(sum(right_list) - sum(left_list))
        
        if difference not in result:
                result[difference] = index
    min_diff = min(result)            
    return result[min_diff]

print(min_index([ 2, 3, 8, 1]))