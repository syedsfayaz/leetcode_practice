'''
Quick Sort
'''


def quick_sort(arry):
    left = []
    right = []
    if len(arry) < 1:
        return arry
    else:
        pivot = len(arry) // 2

    for i in arry:
        if i > arry[pivot]:
            right.append(i)
        else:
            left.append(i)
    return quick_sort(left) + arry[pivot] + quick_sort(right)


arr = [2, 5, 6, 78, 2, 4, 5, 6, 7, 8, 8, 5, 3, 2, 4, 6, 77]
print(quick_sort(arr))
