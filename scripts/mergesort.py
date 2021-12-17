

# from random import randint
# def create_array(array=10,max=50):
#     return [randint(0,max) for _ in range(array)]

#print(create_array())
def merge_sort(a,b):
    final_list = []
    i = j = 0
    while i <= len(a)-1  and j <= len(b)-1:
        if a[i] <= b[j]:
            final_list.append(a[i])
            i += 1
        else:
            final_list.append(b[j])
            j += 1
    return final_list + a[i:] + b[j:]

def merge(arr):
    if len(arr) <= 1: return arr

    left, right = merge(arr[0:int(len(arr)/2)]),merge(arr[int(len(arr)/2):])

    return merge_sort(left, right)


'''inplace merge Sort'''
# from random import randint
#
# def create_array(array=10, max=50):
#     return [randint(0, max) for _ in range(array)]
# #[2, 4, 6, 5, 3, 1]
#
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return
#         # arr
#     mid_val = len(arr) // 2
#     left = arr[:mid_val]
#     right = arr[mid_val:]
#     merge_sort(left)
#     merge_sort(right)
#     merge(left,right, arr)
# #    if len(arr) <= 1:
# #         return
# #     mid = len(arr)//2
# #     left = arr[:mid]
# #     right = arr[mid:]
# #     merge_sort(left)
# #     merge_sort(right)
# #     merge_two_sorted_lists(left, right, arr)
#
# def merge(arr1, arr2, arr):
#     lent1 = len(arr1)
#     lent2 = len(arr2)
#     i = j = k = 0
#     while i < lent1 and j < lent2:
#         if arr1[i] >= arr2[j]:
#             arr[k] = arr2[j]
#             j += 1
#         else:
#             arr[k] = arr[i]
#             i += 1
#         k += 1
#     while i < len(arr1):
#         arr[k] = arr1[i]
#         i += 1
#         k += 1
#     while j < len(arr2):
#         arr[k] = arr2[j]
#         j += 1
#         k += 1

#     len_a = len(a)
#     len_b = len(b)
#     i = j = k = 0
#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             arr[k] = a[i]
#             i+=1
#         else:
#             arr[k] = b[j]
#             j+=1
#         k+=1
#     while i < len_a:
#         arr[k] = a[i]
#         i+=1
#         k+=1
#
#     while j < len_b:
#         arr[k] = b[j]
#         j+=1
#         k+=1
# arr = create_array()
# print(arr)
# merge_sort(arr)
# print(arr)

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return
#
#     mid = len(arr)//2
#
#     left = arr[:mid]
#     right = arr[mid:]
#
#     merge_sort(left)
#     merge_sort(right)
#
#     merge_two_sorted_lists(left, right, arr)
#
# def merge_two_sorted_lists(a,b,arr):
#     len_a = len(a)
#     len_b = len(b)
#
#     i = j = k = 0
#
#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             arr[k] = a[i]
#             i+=1
#         else:
#             arr[k] = b[j]
#             j+=1
#         k+=1
#
#     while i < len_a:
#         arr[k] = a[i]
#         i+=1
#         k+=1
#
#     while j < len_b:
#         arr[k] = b[j]
#         j+=1
#         k+=1
#
if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]
#
    # for arr in test_cases:
    #     print(merge(arr))
    #     #print(arr)

def sortedSquare(input):
    for index, value in enumerate(input):
        input[index] = value**2
    return merge(input)


print(sortedSquare([-2, -1, 0, 2, 3]))


