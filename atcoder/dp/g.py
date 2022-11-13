import sys

sys.setrecursionlimit(500000)
n, m = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(m)]

edge_map = {}
start_points = set()
for x, y in xy:
    if y not in edge_map:
        edge_map[y] = []
    edge_map[y].append(x)
    start_points.add(x)

most_end_points = []

for end_point in edge_map:
    if end_point not in start_points:
        most_end_points.append(end_point)

memo = {}


def solve(end_point):
    if end_point in memo:
        return memo[end_point]
    if end_point not in edge_map:
        result = 0
    else:
        result = max(list(map(solve, edge_map[end_point]))) + 1
    memo[end_point] = result
    return result


print(max(list(map(solve, most_end_points))))
