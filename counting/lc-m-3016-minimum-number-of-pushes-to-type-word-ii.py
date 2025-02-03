from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = list(sorted([(count, letter) for letter, count in Counter(word).items()], reverse=True))

        num_buttons = 8
        pushes = 1
        total_pushes = 0
        for button in range(0, len(counts), num_buttons):
            total_pushes += sum(count for count, _ in counts[button: button + num_buttons]) * pushes
            pushes += 1

        return total_pushes


solution = Solution()
assert solution.minimumPushes("abcde") == 5
assert solution.minimumPushes("xyzxyzxyzxyz") == 12
assert solution.minimumPushes("aabbccddeeffgghhiiiiii") == 24
