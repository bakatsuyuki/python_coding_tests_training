n = int(input())
dcs = [list(map(int, input().split())) for _ in range(n)]
dcs.sort()

max_d = max([d for d, _, _ in dcs])

candidate_ds = {}

for d, c, s in dcs:
    print('開始')
    print(d)
    if d in candidate_ds:
        candidate_ds[d] = max([s, candidate_ds[d]])
    else:
        candidate_ds[d] = s
    for cd in candidate_ds:
        print(cd)
        print(candidate_ds)
        cs = candidate_ds[cd]
        if cd + c <= d:
            candidate_ds[d] = max([candidate_ds[d], s + cs])

print(candidate_ds)

# print(candidate_ds[max_d])
