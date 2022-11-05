import array
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
s = sys.stdin.readline().rstrip()

min_index = 0

s_codes = array.array('b', map(ord, list(s)))
result = []

for i in range(k):
    remain_k = k - i
    sub_s = s_codes[min_index:-remain_k + 1 if remain_k != 1 else None]
    min_value = min(sub_s)
    min_index += sub_s.index(min_value) + 1
    result.append(min_value)

print(''.join(map(chr, result)))
