from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def searchInsert(letters: List[str], target: str) -> int:
            low, high = 0, len(letters)

            while low < high:
                mid = (low + high) // 2

                if letters[mid] <= target:
                    low = mid + 1
                else:
                    high = mid

            return low

        n = len(letters)
        insert_point = searchInsert(letters, target)
        if insert_point == n:
            return letters[0]
        return letters[insert_point]


solution = Solution()
assert solution.nextGreatestLetter(['c', 'f', 'j'], 'a') == 'c'
assert solution.nextGreatestLetter(['c', 'f', 'j'], 'c') == 'f'
assert solution.nextGreatestLetter(['c', 'f', 'j'], 'd') == 'f'
assert solution.nextGreatestLetter(['a', 'b'], 'z') == 'a'
