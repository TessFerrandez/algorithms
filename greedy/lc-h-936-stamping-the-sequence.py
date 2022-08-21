from collections import deque
from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp_len, target_len = len(stamp), len(target)

        queue = deque()
        done = [False] * target_len
        answers, needs_change = [], []

        for idx in range(target_len - stamp_len + 1):
            made, todo = set(), set()

            for stamp_idx, stamp_ch in enumerate(stamp):
                target_ch = target[idx + stamp_idx]
                if target_ch == stamp_ch:
                    made.add(idx + stamp_idx)
                else:
                    todo.add(idx + stamp_idx)
            needs_change.append((made, todo))

            # If we can reverse stamp at i immediately,
            # enqueue letters from this window.
            if not todo:
                answers.append(idx)
                for stamp_idx in range(idx, idx + len(stamp)):
                    if not done[stamp_idx]:
                        queue.append(stamp_idx)
                        done[stamp_idx] = True

        # For each enqueued letter,
        while queue:
            idx = queue.popleft()

            # For each window that is potentially affected,
            # j: start of window
            for stamp_idx in range(max(0, idx - stamp_len + 1), min(target_len - stamp_len, idx) + 1):
                if idx in needs_change[stamp_idx][1]:           # This window is affected
                    needs_change[stamp_idx][1].discard(idx)     # Remove it from todo list of this window
                    if not needs_change[stamp_idx][1]:          # Todo list of this window is empty
                        answers.append(stamp_idx)
                        for i in needs_change[stamp_idx][0]:    # For each letter to potentially enqueue,
                            if not done[i]:
                                queue.append(i)
                                done[i] = True

        return answers[::-1] if all(done) else []


solution = Solution()
assert solution.movesToStamp("abc", "ababc") == [1, 0, 2]
assert solution.movesToStamp("abca", "aabcaca") == [2, 3, 0, 1]
