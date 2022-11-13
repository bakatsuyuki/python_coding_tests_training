n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]


class UnionFind:
    def __init__(self):
        self.parents = {}

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        self.parents[root1] = root2

    def find(self, node):
        if node not in self.parents or node == self.parents[node]:
            self.parents[node] = node
            return node
        else:
            parent_node = self.parents[node]
            root_node = self.find(parent_node)
            self.parents[node] = root_node
            return root_node

    def group(self, node):
        root = self.find(node)
        return [key for i, key in enumerate(self.parents) if self.find(self.parents[key]) == root]


uf = UnionFind()

floor_map = {}
for a, b in ab:
    uf.union(a, b)

print(max(uf.group(1)))
