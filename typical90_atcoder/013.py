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
        for destination in load_map[index]:
            if destination in settled_indexes:
                continue
            cost = load_map[index][destination]
            costs[destination] = min(costs[destination], costs[index] + cost)
        min_cost = inf
        min_index = None
        for i, cost in [[i, cost] for i, cost in enumerate(costs) if i not in settled_indexes]:
            if cost < min_cost:
                min_index = i
                min_cost = cost
        settled_indexes.append(min_index)
        index = min_index
    return costs


dijkstra_forward = dijkstra(1)
dijkstra_reverse = dijkstra(n)

for i in range(1, n + 1):
    print(dijkstra_forward[i] + dijkstra_reverse[i])
