# import collections
#
# s = input().strip()
# freq = collections.Counter(s)
# values = list(freq.values())
# values.sort()
# print('YES' if values.count(values[0]) == len(values) or (values.count(values[0]) == len(values) - 1 and values[-1] - values[-2] == 1)


array1 = [1, 2, 3, 4, 5, 6]
array2 = [3, 4, 6, 7, 8]
k = []
i = j = 0
while i < len(array1):
    try:
        if array2[j] and array1[i] < array2[j]:
            k.append(array1[i])
            i += 1
        elif arrar2[j] and array1[i] > array2[j]:
            k.append(array2[j])
            j += 1
        else:
            k.append(array1[i])
            k.append(array2[j])
            i = j = +1
    except:
        k.append(array1[i:])
        k.append(array2[j:])
print(k)
