def strhash(s):
    h = 0
    for c in s:
        h += hash(c)
    return(h)

def seqsum(n):
    return int((n**2 + n) / 2)

def sherlockAndAnagrams(s):
    count = 0
    for l in range(len(s)):
        counter = dict()
        #l is length of substr.
        for i in range(len(s)-l):
            hashed = strhash(s[i:i+l+1])
            if hashed not in counter:
                counter[hashed] = 1
            else: 
                counter[hashed] += 1
        for k,v in counter.items():
            if v > 1:
                count += seqsum(v-1)
    print(count)
    return count