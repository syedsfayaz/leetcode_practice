
from random import randint
def create_arry(max=50,length=10):
    return [randint(0,max) for _ in range(length)]

# def quick_sort(a):
#     if len(a) <= 1: return a
#     small,equal,large = [],[],[]
#     pivot = a[randint(0,len(a)-1)]
#     for i in a:
#         if i < pivot: small.append(i)
#         elif i > pivot: large.append(i)
#         else: equal.append(i)
#     return quick_sort(small)+equal+quick_sort(large)

def quick_sort(a):
    if len(a) <= 1: return a
    pivot = len(a) // 2
    small, equal, large = [], [], []
    for i in range(len(a)):
        if a[i] > a[pivot]:
            large.append(a[i])
        elif a[i] < a[pivot]:
            small.append(a[i])
        else:
            equal.append(a[i])
        return quick_sort(small) + equal + quick_sort(large)



arr = create_arry()
print(arr)
print(quick_sort(arr))
