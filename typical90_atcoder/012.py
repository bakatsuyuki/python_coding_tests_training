# sys.stdin = open('typical90_l_in_subtask_1_35.txt')

h, w = map(int, input().split())
q_count = int(input())
q = [list(map(int, input().split())) for _ in range(q_count)]

red_points_map = {}
list_ref = []

root_point = [-1, -1]


class UnionFind:
    def __init__(self):
        self.parents = [[root_point for _ in range(w + 2)] for _ in range(h + 2)]

    def find(self, point):
        x, y = point
        parent_point = self.parents[x][y]
        if parent_point == root_point:
            return root_point
        elif parent_point == point:
            return point
        else:
            node = self.find(parent_point)
            return node

    def same(self, point_a, point_b):
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        if root_a == root_point or root_b == root_point:
            return False
        return self.find(point_a) == self.find(point_b)

    def union(self, point_a, point_b):
        if point_a == root_point or point_b == root_point:
            return
        bx, by = self.find(point_b)
        self.parents[bx][by] = self.find(point_a)

    def add(self, point):
        x, y = point
        self.parents[x][y] = point


uf = UnionFind()


def point_to_key(r, c):
    return f'{r} {c}'


def key_to_point(key):
    return map(int, key.split())


def query_1(arguments):
    r, c = arguments

    points = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]

    uf.add(arguments)
    for point in points:
        point_node = uf.find(point)
        if point_node != root_point:
            uf.union(point_node, [r, c])


def query_2(arguments):
    ra, ca, rb, cb = arguments
    if uf.same([ra, ca], [rb, cb]):
        print('Yes')
    else:
        print('No')


for query in q:
    if query[0] == 1:
        query_1(query[1:])
    if query[0] == 2:
        query_2(query[1:])
