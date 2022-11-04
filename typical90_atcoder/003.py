import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline().rstrip())
a = {}
for i in range(n - 1):
    a1, a2 = list(map(int, sys.stdin.readline().rstrip().split()))
    if a1 not in a:
        a[a1] = [a2]
    else:
        a[a1].append(a2)
    if a2 not in a:
        a[a2] = [a1]
    else:
        a[a2].append(a1)

current_index = min(a)
queue = [current_index]


def calc_distances(start_at):
    def dfs(index, distance, before_index):
        distances[index] = distance
        for next_index in a[index]:
            if next_index == before_index or next_index in distances:
                continue
            dfs(next_index, distance + 1, index)

    distances = {}
    dfs(start_at, 0, None)
    return distances


tmp_distances = calc_distances(min(a))
tmp_max_key = max(tmp_distances, key=tmp_distances.get)
result_distances = calc_distances(tmp_max_key)
result_max_key = max(result_distances, key=result_distances.get)
print(result_distances[result_max_key] + 1)
