class Solution:
    # brute force - ok
    def secondsToRemoveOccurrences1(self, s: str) -> int:
        count = 0
        idx = s.find('01')
        while idx != -1:
            s = s.replace('01', '10')
            count += 1
            idx = s.find('01')
        return count

    # better - based on how many steps you need to move the last 1
    def secondsToRemoveOccurrences(self, s: str) -> int:
        '''
        1. to move an '1' at the ith index, takes x steps where x is number of 0 preceding it
        2. if there is a '1' at 'i-1'st index, it takes at least one more step to move this '1' to the proper position
        '''
        steps = zeros = 0

        for ch in s:
            if ch == '0':
                zeros += 1
                continue
            if zeros > 0:
                steps = max(1 + steps, zeros)

        return steps


solution = Solution()
assert solution.secondsToRemoveOccurrences("0110101") == 4
assert solution.secondsToRemoveOccurrences("11100") == 0
