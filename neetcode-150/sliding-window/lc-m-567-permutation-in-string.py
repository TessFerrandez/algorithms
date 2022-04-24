class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1n = len(s1)

        if len(s2) < len(s1):
            return False

        counts = [0 for _ in range(26)]
        window = [0 for _ in range(26)]

        for i in range(s1n):
            counts[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2) - s1n):
            if window == counts:
                return True
            window[ord(s2[i + s1n]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] -= 1

        return window == counts


solution = Solution()
assert solution.checkInclusion('ab', 'eidbaooo')
assert not solution.checkInclusion('ab', 'eidboaoo')
assert solution.checkInclusion('ab', 'eidboaooab')
