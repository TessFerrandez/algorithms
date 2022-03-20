class Solution:
    def countCollisions2(self, directions: str) -> int:
        n = len(directions)

        i = 0
        while i < n and directions[i] == 'L':
            i += 1

        dont_count = i

        i = n - 1
        while i >= 0 and directions[i] == 'R':
            i -= 1

        dont_count += n - 1 - i

        return directions.count('L') + directions.count('R') - dont_count

    def countCollisions1(self, directions: str) -> int:
        n = len(directions)

        left = 0
        while left < n and directions[left] == 'L':
            left += 1

        right = n - 1
        while right >= 0 and directions[right] == 'R':
            right -= 1

        return directions[left: right + 1].count('L') + directions[left: right + 1].count('R')

    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L')
        directions = directions.rstrip('R')
        return len(directions) - directions.count('S')


solution = Solution()
assert solution.countCollisions('SRRLRLRSRLRSSRRLSLRLLRSLSLLSSRRLSRSLSLRRS') == 28
assert solution.countCollisions('LLRR') == 0
assert solution.countCollisions('SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR') == 20
assert solution.countCollisions('RLRSLL') == 5
