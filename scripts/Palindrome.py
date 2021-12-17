
def palindrome(array):
    lenghtofS = len(array)
    oddcount = 0
    pairs = set(array)
    for i in pairs:
       if array.count(i) % 2 != 0:
          oddcount += 1

    if oddcount < 2:
        return('Yes')
    else:
        return('No')
print(palindrome('carrace'))

def is_palindrome(array):
    #return array == array[::-1]
    rev = ''.join(reversed(array))
    if array == rev: return True
    return False
print(is_palindrome('araa'))



