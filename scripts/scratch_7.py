

# def merge(left, right):
#     l1,l2 = left, right
#     l3 = []
#     i = j = 0
#     while i < len(l1) and j < len(l2):
#         if l1[i] > l2[j]:
#             l3 = l3 + [l2[j]]
#             j += 1
#         elif l1[i] < l2[j]:
#             l3 = l3 + [l1[i]]
#             i  += 1
#         else:
#             l3 = l3 + [l1[i]] + [l2[j]]
#             i += 1
#             j += 1
#
#     l3 = l3 + l1[i:] + l2[j:]
#     return(l3)
#
# def merge_sort(ordered):
#     if len(ordered) <= 1:
#         return ordered
#     mid_value = int(len(ordered)/2)
#     left = merge_sort(ordered[:mid_value])
#     right = merge_sort(ordered[mid_value:])
#     return merge(left, right)
#
# ordered = [5,6,2,5,7,9,2,43,7,75,84,34,63,63,3,-3,-5,-6,-9]
# print(merge_sort(ordered))


# l1 = [6,-2,1,5,-4]
#
#
# # #### Bubble Sort
# def sorting(l1):
    # for i in range(len(l1) - 1):
    #     if l1[i] > l1[i+1]:
    #         l1[i],l1[i+1] = l1[i+1],l1[i]
    #         sorting(l1)
    # return(l1)
#     sorted = True
#     while sorted:
#         sorted = False
#         for i in range(len(l1) - 1):
#             if l1[i] > l1[i+1]:
#                l1[i],l1[i+1] = l1[i+1],l1[i]
#                sorted = True
# #     return(l1)
# print(sorting(l1))

##### Selection Sort
#
# def selection_sort(l1):
#
#     for i in range(len(l1)-1):
#         min_value = i
#         for j in range(i+1, len(l1)):
#             if l1[j] < l1[min_value]:
#                 min_value = j
#         if min_value != i:
#             l1[min_value],l1[i] = l1[i],l1[min_value]
#     return l1
#
# print(selection_sort(l1))


### quick Sorting
# def quick_sort(sequence):
#     length = len(sequence)
#     mid = int(len(sequence)/2)
#     if length <= 1:
#         return sequence
#     else:
#         pivot = sequence.pop(mid)
#
#     items_greater = []
#     items_lower = []
#
#     for items in sequence:
#         if items > pivot:
#             items_greater.append(items)
#         else:
#             items_lower.append(items)
#     return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
#
# print(quick_sort([5,8,6,9,4,7,8,3,5,6,7,8,8,5,4,3,35,6,7, -2, -4, -7, -8]))


###### Binary search

# def binary_search(sequence, item):
#     # mid_value = int(len(sequence) / 2)
#     # first_items = sequence[:mid_value]
#     # second_items = sequence[mid_value:]
#     # #print(sequence[mid_value])
#     # if item == int(sequence[mid_value]):
#     #     return "Exists"
#     # elif item > sequence[mid_value]:
#     #     return binary_search(second_items, item)
#     # else:
#     #    return binary_search(first_items, item)
#     # return None
#
#     begin_index = 0
#     end_index = len(sequence) -1
#     while begin_index <= end_index:
#         mid_point = begin_index + (end_index - begin_index) // 2
#         mid_point_value = sequence[mid_point]
#         if mid_point_value == item:
#             return mid_point
#         elif mid_point_value > item:
#             end_index = mid_point - 1
#         else:
#             begin_index = mid_point + 1
#     return None

#
# def mission_number(sequence):
#
#     begin_index = 0
#     end_index = len(sequence) -1
#     while begin_index <= end_index:
#         mid_point = begin_index + (end_index - begin_index) // 2
#         mid_point_value = sequence[mid_point]
#         if mid_point_value == mid_point + 1:
#             begin_index = mid_point + 1
#         else:
#             end_index = mid_point - 1
#     return mid_point_value
# kist = [1, 2, 3, 4, 6, 7, 8, 9, 10]
# item = 8
# print(mission_number(kist))

############################################################################
#################### Sliding window#########################################
############################################################################
'''
Maximum sum
'''
numbers = [2,3,4,5,-1,7,8,9,0,4,7,-7,3]
k = 3
def maximum_summ(numbers, k):
    maximum_sum  = 0
    total_sum = sum(numbers[:k])
    i = 3
    while i < len(numbers) - 1:
        x = (numbers[i-k])
        y = (numbers[i])
        total_sum = total_sum - numbers[i-k] + numbers[i]
        maximum_sum = max(total_sum, maximum_sum)
        i += 1
    return maximum_sum

print(maximum_summ(numbers,k))
'''
Find smallest subarray of sum k
'''
numbers = [2,3,4,5,1,7,1,9,0,4,7,7,3]
k = 8

def smallest_subarray(numbers, k):
        lengthofArray = len(numbers) + 1
        total_sum = 0
        i = j = 0
        while i < len(numbers):
            total_sum += numbers[i]
            i += 1
            while total_sum >= k:
                total_sum -= numbers[j]
                j += 1
                lengthofArray = min(i-j + 1, lengthofArray)
        return lengthofArray
print(smallest_subarray(numbers,k))










