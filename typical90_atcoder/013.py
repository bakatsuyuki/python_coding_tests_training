import _pickle
import heapq

# from line_profiler_pycharm import profile

# sys.stdin = open('typical90_m_in_killer_2.txt')
n, m = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]

raw_load_map = {}

inf = 10 ** 9

for a, b, c in abc:
    if a not in raw_load_map:
        raw_load_map[a] = {}
    if b not in raw_load_map:
        raw_load_map[b] = {}
    raw_load_map[a][b] = c
    raw_load_map[b][a] = c


# @profile
def dijkstra(start_at):
    load_map = _pickle.loads(_pickle.dumps(raw_load_map, -1))
    settled_indexes = []
    costs = {}
    settled_indexes.append(start_at)
    unsettled_costs = []
    heapq.heappush(unsettled_costs, [0, start_at])
    while unsettled_costs:
        cost, index = heapq.heappop(unsettled_costs)
        if index in costs:
            continue
        costs[index] = cost
        for destination in load_map[index]:
            heapq.heappush(unsettled_costs, [cost + load_map[index][destination], destination])
    return costs


dijkstra_forward = dijkstra(1)
dijkstra_reverse = dijkstra(n)

for i in range(1, n + 1):
    print(dijkstra_forward[i] + dijkstra_reverse[i])
