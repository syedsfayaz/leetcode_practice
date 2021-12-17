import math
import os
import random
import re
import sys
from collections import Counter
queries = [[1, 3],[2, 3],[3, 2],[1, 4],[1, 5],[1, 5],[1, 4],[3, 2],[2, 4],[3, 2]]

from collections import defaultdict
def freqQuery(queries):

    d = defaultdict(int) ; f = defaultdict(set)

    for (c,v) in queries:
        if c==3 : yield int( len(f[v])>0 ) ; continue

        f[d[v]].discard(v)
        if c==1 : d[v] += 1
        elif d[v]>0 : d[v] -= 1
        f[d[v]].add(v)
    print(d)



# def freqQuery(queries):
#     freq = Counter()  # freq = {3: 1}
#     cnt = Counter()   # cnt = {3: -1, }
#     arr = []
#     for q in queries:
#         if q[0]==1:
#             cnt[freq[q[1]]]-=1
#             #print(cnt[freq[q[1]]])
#             freq[q[1]]+=1
#             cnt[freq[q[1]]]+=1
#             #print(cnt[freq[q[1]]])
#         elif q[0]==2:
#             if freq[q[1]]>0:
#                 cnt[freq[q[1]]]-=1
#                 freq[q[1]]-=1
#                 cnt[freq[q[1]]]+=1
#
#         else:
#             if cnt[q[1]]>0:
#                 arr.append(1)
#             else:
#                 arr.append(0)
#
#     print(arr)



freqQuery(queries)