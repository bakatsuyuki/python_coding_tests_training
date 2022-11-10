import heapq
from typing import List


class ReverseHeap:
    max_value = 1000

    def __init__(self, data):
        reversed_list = list(map(self.get_reversed_value, data))
        heapq.heapify(reversed_list)
        self.data = reversed_list

    def pop(self):
        return self.max_value - heapq.heappop(self.data)

    def push(self, new_value):
        heapq.heappush(self.data, self.get_reversed_value(new_value))

    def get_reversed_value(self, value):
        return self.max_value - value

    def count(self):
        return len(self.data)


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        reverse_heap = ReverseHeap(stones)
        while reverse_heap.count() > 1:
            value1 = reverse_heap.pop()
            value2 = reverse_heap.pop()
            print(value1, value2)
            new_value = value1 - value2
            if new_value != 0:
                reverse_heap.push(new_value)

        if reverse_heap.count() == 0:
            return 0
        return reverse_heap.pop()


print(Solution().lastStoneWeightII([31, 26, 33, 21, 40]))
