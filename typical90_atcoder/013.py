n, m = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]

load_map = {}

inf = 10 ** 9

for a, b, c in abc:
    if a not in load_map:
        load_map[a] = {}
    if b not in load_map:
        load_map[b] = {}
    load_map[a][b] = c
    load_map[b][a] = c


def dijkstra(start_at):
    settled_indexes = []
    costs = [inf] * (n + 1)
    costs[start_at] = 0
    settled_indexes.append(start_at)
    index = start_at
    while len(settled_indexes) < n:
        min_new_cost = inf
        min_new_index = None
        for destination in load_map[index]:
            if destination in settled_indexes:
                continue
            cost = load_map[index][destination]
            costs[destination] = min(costs[destination], costs[index] + cost)
            if costs[destination] < min_new_cost:
                min_new_cost = costs[destination]
                min_new_index = destination
        settled_indexes.append(min_new_index)
        index = min_new_index
    return costs


dijkstra_all = dijkstra(1)
dijkstra_reverse = dijkstra(n)

print(dijkstra_all)
print(dijkstra_reverse)

for i in range(1, n + 1):
    print(dijkstra_all[i] + dijkstra_reverse[i])
