'''
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.
'''
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        to_visit = set(room for room in range(1, len(rooms)))

        keys = rooms[0][::]
        while keys:
            room = keys.pop()
            if room in to_visit:
                for key in rooms[room]:
                    if key in to_visit and key != room:
                        keys.append(key)
                to_visit.remove(room)

        return len(to_visit) == 0


solution = Solution()
assert solution.canVisitAllRooms([[1], [2], [3], []])
assert not solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
