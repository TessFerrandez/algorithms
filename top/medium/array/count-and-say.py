class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        prev = self.countAndSay(n - 1)

        last = '0'
        count = 0

        result = ''
        for ch in prev:
            if ch == last:
                count += 1
            else:
                if count != 0:
                    result += str(count) + last
                last = ch
                count = 1

        if count != 0:
            result += str(count) + last

        return result


solution = Solution()
assert solution.countAndSay(1) == '1'
assert solution.countAndSay(4) == '1211'
