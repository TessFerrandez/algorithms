class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        big = 10 ** 4

        bulky = length >= big or width >= big or height >= big or (length * width * height) >= 10 ** 9
        heavy = mass >= 100

        if bulky and heavy:
            return 'Both'
        elif not bulky and not heavy:
            return 'Neither'
        elif bulky:
            return 'Bulky'
        else:
            return 'Heavy'


solution = Solution()
assert solution.categorizeBox(length=1000, width=35, height=700, mass=300) == 'Heavy'
assert solution.categorizeBox(length=200, width=50, height=800, mass=50) == 'Neither'
