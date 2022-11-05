import sys
from array import array

# sys.stdin = open('typical90_g_in_max_random02.txt')
n = int(sys.stdin.readline().rstrip())
raw_a = list(map(int, sys.stdin.readline().rstrip().split()))
q = int(sys.stdin.readline().rstrip())
b = [int(sys.stdin.readline().rstrip()) for _ in range(q)]

raw_a.sort()
a = array('i', raw_a)
min_a = a[0]
max_a = a[-1]
a_min_index = 0
a_max_index = len(a) - 1


def binary_search(b_value):
    min_dif = min_a - b_value
    max_dif = max_a - b_value
    if max_dif < 0:
        return abs(max_dif)
    if min_dif > 0:
        return min_dif

    min_index = a_min_index
    max_index = a_max_index
    while max_index - min_index > 1:
        index = (max_index + min_index) // 2
        dif = a[index] - b_value
        if dif < 0:
            min_index = index
        elif dif > 0:
            max_index = index
        else:
            return 0

    result = min(abs(a[min_index] - b_value), a[max_index] - b_value)
    return result


min_list = [binary_search(b_value) for b_value in b]

text = '\n'.join(map(str, min_list))
sys.stdout.writelines(text)
