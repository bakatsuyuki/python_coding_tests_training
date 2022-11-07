n, m = map(int, input().split())
lr = [map(int, input().split()) for _ in range(m)]

lr.sort()

for i in range(1, n + 1):
    lr.pop(0)

