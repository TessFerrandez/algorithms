from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        counts = Counter(s)

        numbers = []
        criteria = [('z', 'zero', 0),('w', 'two', 2),('u', 'four', 4),('o', 'one', 1),('r', 'three', 3),('f', 'five', 5),('x', 'six', 6),('v', 'seven', 7),('g', 'eight', 8),('n', 'nine', 9)]
        for ch, word, number in criteria:
            while counts[ch] > 0:
                for char in word:
                    counts[char] -= 1
                numbers.append(number)

        numbers.sort()
        return ''.join(str(num) for num in numbers)


solution = Solution()
assert solution.originalDigits("owoztneoer") == "012"
assert solution.originalDigits("fviefuro") == "45"
assert solution.originalDigits('nine') == '9'
