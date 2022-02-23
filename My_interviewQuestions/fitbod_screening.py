# Given plates of 2.5lb, 5lb, 10lb, 25lb, 35lb, 45lb, what plates do you #need for 165lbs given a 45lb barbell?

# Write a function that returns the number of each plate needed resulting in #the least plates used.

# Plates should be balanced on both sides of the barbell:
# 1. Weight on the left = weight on the right
# 2. Plate types used should be in pairs.

## 165  - 45 = 120  ==60

# from collections import defaultdict

weights = [2.5, 5.0, 10.0, 25.0, 35.0, 45.0]


# TODO: Write code here
def calculate_plates(target_weight):
    result = {}
    count = 0
    weight_needed = abs((45.0 - target_weight) / 2)
    i = len(weights) - 1
    while i > 0:
        if weights[i] <= weight_needed:
            if weights[i] not in result:
                result[weights[i]] = 0
            result[weights[i]] += 1
            count += 1
            weight_needed = abs(weights[i] - weight_needed)
            # print(weight_needed)
        i -= 1

        if weight_needed == 0:
            return result

    return result


print(calculate_plates(165.0))
