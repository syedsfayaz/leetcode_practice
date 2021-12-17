from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dicta = Counter(a)
    dictb = Counter(b)
    count = 0
    #print(dicta,dictb)
    for key,value in dicta.items():
        if key in dictb:
            count += abs(dictb[key] - value)
            #print(count)
        else:
            count += value
            #print(count)
    for key,value in dictb.items():
        if key not in dicta:
            count += value
            #print(count)
        # else:
        #     count += value
    print(count)

a = "cde"
b = "abc"

makeAnagram(a, b)