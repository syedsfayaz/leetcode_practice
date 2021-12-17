from random import randint
def create_array(array=10,max=50):
    return [randint(0,max) for _ in range(array)]

def selection_sort(arr):
    #min_value = -1
    index = 0
    while index < len(arr) -1:
        min_value = index
        for j in range(index,len(arr)-1):
            if arr[j] < arr[min_value]:
                min_value = j
        if arr[min_value] != arr[index]:
            arr[index], arr[min_value] = arr[min_value], arr[index]
        index += 1
    return arr


# arr = [5,6,4,3,2,5,6]
# print(selection_sort(arr))
arr = create_array()
print(selection_sort(arr))