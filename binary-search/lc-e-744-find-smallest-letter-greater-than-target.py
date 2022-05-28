from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters)

        while low < high:
            mid = (low + high) // 2

            if letters[mid] > target:
                high = mid
            else:
                low = mid + 1

        if low == len(letters):
            return letters[0]
        return letters[low]


solution = Solution()
assert solution.nextGreatestLetter(['c', 'f', 'j'], 'a') == 'c'
assert solution.nextGreatestLetter(['c', 'f', 'j'], 'c') == 'f'
assert solution.nextGreatestLetter(['c', 'f', 'j'], 'd') == 'f'
assert solution.nextGreatestLetter(['a', 'b'], 'z') == 'a'
