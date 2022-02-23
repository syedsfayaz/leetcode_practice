## Start typing here
# Write a function that takes in non-empty of arbitrary intervals, merge any overlapping intervals, and returns the new intervals
# in no particular order.

# Sample input: [[1,2], [3,5], [9,10], [4,7], [6,8]]

'''
[[1,2], [3,5], [4,7], [6,8], [9,10]]

'''


# ouput: [ [1,2], [3,8], [9,10]]

def mergeOverlappingIntervals(intervals):
    if len(intervals) == 0:
        return None
    output = []
    temp_sort = sorted(intervals, key=lambda item:item[0])
    print(temp_sort)
    for items in temp_sort:
        if output and items[0] <= output[-1][1]:
            output[-1][1] = items[0]
        else:
            output.append(items)
    return output

print(mergeOverlappingIntervals([[1,2], [3,5], [9,10], [4,7], [6,8]]))


