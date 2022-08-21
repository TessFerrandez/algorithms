from heapq import heapify, heappop, heappush
from typing import Counter, List


class Solution:
    # note: have to think backwards since pythons heap is min heap
    # so we have to store -freq
    def leastInterval(self, tasks: List[str], n: int) -> int:
        todo = [(-freq, task) for task, freq in Counter(tasks).items()]
        heapify(todo)

        cycles = 0
        while todo:
            wait_time = n + 1
            possible_todo = []

            while wait_time > 0 and todo:
                freq, task = heappop(todo)
                possible_todo.append((freq + 1, task))
                wait_time -= 1
                cycles += 1          # successfully executed task

            for freq, task in possible_todo:
                if freq < 0:
                    heappush(todo, (freq, task))

            if not todo:
                break

            cycles += wait_time      # if wait_time > 0 we need to idle

        return cycles


solution = Solution()
assert solution.leastInterval(["A","A","A","B","B","B"], 2) == 8
assert solution.leastInterval(["A","A","A","B","B","B"], 0) == 6
assert solution.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) == 16
