class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0
        result = ""
        while idx < len(word1) and idx < len(word2):
            result += word1[idx]
            result += word2[idx]
            idx += 1
        if idx < len(word1):
            result += word1[idx:]
        elif idx < len(word2):
            result += word2[idx:]
        return result


solution = Solution()
assert solution.mergeAlternately("abc", "pqr") == "apbqcr"
assert solution.mergeAlternately("ab", "pqrs") == "apbqrs"
assert solution.mergeAlternately("abcd", "pq") == "apbqcd"
