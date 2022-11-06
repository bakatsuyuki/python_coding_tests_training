import sys

# sys.stdin = open('typical90_j_in_hand05.txt')
n = int(input())
cp = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

sum_cache = {}

a = [0] * n
b = [0] * n
c, p = cp[0]
if c == 1:
    a[0] = p
else:
    b[0] = p

for i in range(1, len(cp)):
    c, p = cp[i]
    if c == 1:
        a[i] = a[i - 1] + p
        b[i] = b[i - 1]
    else:
        a[i] = a[i - 1]
        b[i] = b[i - 1] + p


def sum_with_range(l, r):
    if l == 0:
        result = [a[r], b[r]]
    else:
        result = [a[r] - a[l - 1], b[r] - b[l - 1]]
    return result


answers = [sum_with_range(l - 1, r - 1) for l, r in lr]

sys.stdout.writelines('\n'.join(map(lambda points: f'{points[0]} {points[1]}', answers)))
