n = int(input())
abc = list(map(int, input().split()))
abc.sort()
a, b, c = abc

score = 10000
for i in reversed(range(n // c + 1)):
    remain_ba = n - c * i
    if score <= i + remain_ba // b:
        break
    for j in reversed(range(remain_ba // b + 1)):
        remain_a = remain_ba - b * j
        if score <= remain_a // a + i + j:
            break
        if remain_a % a == 0:
            score = min(score, remain_a // a + i + j)

print(score)
