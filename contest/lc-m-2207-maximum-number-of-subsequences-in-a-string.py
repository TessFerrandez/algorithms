class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        index_a, index_b = [], []
        a, b = pattern[0], pattern[1]

        # if pattern is ab - record the indices of a and b
        for i, ch in enumerate(text):
            if ch == a:
                index_a.append(i)
            if ch == b:
                index_b.append(i)

        j = 0
        count = 0

        # continue adding up the number of times a occurrs before any instances of b
        subsequence_matches = len(index_b)
        for i in index_b:
            while j < len(index_a) and index_a[j] < i:
                count += subsequence_matches
                j += 1
            subsequence_matches -= 1

        count += max(len(index_a), len(index_b))
        return count


solution = Solution()
assert solution.maximumSubsequenceCount('abdcdbc', 'ac') == 4
assert solution.maximumSubsequenceCount('aabb', 'ab')
