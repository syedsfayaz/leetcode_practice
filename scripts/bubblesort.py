from random import randint
def create_array(array=10,max=50):
    return [randint(0,max) for _ in range(array)]

# def bubble_sort(arr):
#     sorting = True
#     while sorting:
#         sorting = False
#         for i in range(len(arr) -1 ):
#             if arr[i] > arr[i+1]:
#                 arr[i],arr[i+1] = arr[i+1],arr[i]
#                 sorting=True
#     return arr

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] >= arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = create_array()
print(arr)
print(bubble_sort(arr))