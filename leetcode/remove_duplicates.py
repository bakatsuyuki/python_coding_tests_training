from line_profiler_pycharm import profile

duplicates = {f'{chr(i)}{chr(i)}' for i in range(97, 123)}


class Node:
    def __init__(self, data):
        self.data = data
        self.child = None
        self.parent = None

    def combine(self, node):
        if self.data == node.data:
            self.parent.child = None
            return self.parent
        else:
            self.child = node
            node.parent = self
            return node

    def get_text(self):
        if self.child is None:
            return self.data
        return self.data + self.child.get_text()


class Solution:
    @profile
    def removeDuplicates(self, s: str) -> str:
        for index in reversed(range(len(s) - 1)):
            if index >= len(s) - 1:
                continue
            if s[index] == s[index + 1]:
                s = s[0: index] + s[index + 2:]
        return s

    @profile
    def removeDuplicatesOld(self, s: str) -> str:
        index = 0
        while index < len(s) - 1:
            if s[index] == s[index + 1]:
                s = s[0: index] + s[index + 2:]
                index = max(index - 1, 0)
            else:
                index += 1
        return s


t = input()
print(Solution().removeDuplicates(t))
print(Solution().removeDuplicatesOld(t))
