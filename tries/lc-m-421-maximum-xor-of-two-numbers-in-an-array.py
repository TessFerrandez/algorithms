from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, num):
        current = self.root

        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in current.children:
                current.children[bit] = TrieNode()
            current = current.children[bit]

    def find_max_xor(self, num):
        current = self.root

        result = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            complement = 1 - bit
            if complement in current.children:
                result += 1 << i
                current = current.children[complement]
            else:
                current = current.children[bit]

        return result

    def find_max(self, nums):
        result = 0

        for num in nums:
            self.insert(num)
            value = self.find_max_xor(num)
            result = max(result, value)

        return result


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        return trie.find_max(nums)


solution = Solution()
assert solution.findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28
assert solution.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]) == 127
