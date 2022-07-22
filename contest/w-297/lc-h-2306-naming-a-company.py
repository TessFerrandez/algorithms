from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # group strings by their initials
        dict = [set() for _ in range(26)]
        for idea in ideas:
            dict[ord(idea[0]) - ord('a')].add(idea[1:])

        answer = 0
        # calculate number of valid names from every initial pair
        for i in range(25):
            for j in range(i + 1, 26):
                k = len(dict[i] & dict[j])      # number of duplicated suffixes
                answer += 2 * (len(dict[i]) - k) * (len(dict[j]) - k)
        return answer


solution = Solution()
assert solution.distinctNames(["coffee","donuts","time","toffee"]) == 6
assert solution.distinctNames(["lack","back"]) == 0
