from collections import deque

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ladder_map = {}

for a, b in ab:
    if a not in ladder_map:
        ladder_map[a] = []
    if b not in ladder_map:
        ladder_map[b] = []
    ladder_map[a].append(b)
    ladder_map[b].append(a)

reachable_floor_set = set()

que = deque([])

que.append(1)
if 1 not in ladder_map:
    print(1)
    exit()

while que:
    floor = que.pop()
    reachable_floor_set.add(floor)
    for next_floor in ladder_map[floor]:
        if next_floor not in reachable_floor_set and next_floor not in que:
            que.append(next_floor)

print(max(reachable_floor_set))
