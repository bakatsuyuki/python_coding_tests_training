import _pickle
import sys
from array import array

from line_profiler_pycharm import profile

sys.stdin = open('typical90_m_in_killer_2.txt')
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


@profile
def dijkstra(start_at):
    load_map = _pickle.loads(_pickle.dumps(raw_load_map, -1))
    unsettled_costs = {}
    settled_indexes = array('i', [])
    costs = {start_at: 0}
    settled_indexes.append(start_at)
    index = start_at
    loop_count = 0

    loop_count2 = 0
    outer_loop_count = 0
    for _ in range(n - 1):
        destinations = []
        outer_loop_count += 1
        for destination in load_map[index]:
            loop_count += 1
            if destination not in unsettled_costs:
                unsettled_costs[destination] = inf
            cost = load_map[index][destination]
            unsettled_costs[destination] = min(unsettled_costs[destination], costs[index] + cost)
            destinations.append(destination)
        del load_map[index]
        for destination in destinations:
            loop_count2 += 1
            del load_map[destination][index]
        min_index = min(unsettled_costs, key=unsettled_costs.get)
        settled_indexes.append(min_index)
        index = min_index
        costs[index] = unsettled_costs[min_index]
        del unsettled_costs[min_index]
    return costs


dijkstra_forward = dijkstra(1)
dijkstra_reverse = dijkstra(n)

for i in range(1, n + 1):
    print(dijkstra_forward[i] + dijkstra_reverse[i])
