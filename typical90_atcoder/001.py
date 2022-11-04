import math

n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

pieces = []
for i in range(n):
    if i == 0:
        pieces.append(a[i])
    else:
        pieces.append(a[i] - a[i - 1])
pieces.append(l - a[n - 1])

min_score = min(pieces)
max_score = math.floor(l / (k + 1))

while max_score != min_score:
    i = math.floor((max_score + min_score) / 2)
    if min_score == i:
        i += 1
    tmp = i
    cut_count = -1
    for piece in pieces:
        if tmp >= i:
            tmp = piece
            cut_count += 1
        else:
            tmp += piece
    last_peace = tmp
    if cut_count > k:
        min_score = i
    if (tmp < i and cut_count <= k) or cut_count < k:
        max_score = i - 1
    else:
        min_score = i
print(min_score)
