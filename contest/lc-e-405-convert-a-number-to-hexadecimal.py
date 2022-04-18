class Solution:
    # using builtins
    def toHex1(self, num: int) -> str:
        if num == 0:
            return '0'
        if num > 0:
            return hex(num)[2:]
        else:
            return str("0x%08X" % (num & 0xffffffff))[2:].lower()

    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        mp = '0123456789abcdef'  # like a map
        answer = ''

        for _ in range(8):
            n = num & 15            # this means num & 1111b
            c = mp[n]               # get the hex char
            answer = c + answer
            num = num >> 4
        return answer.lstrip('0')   # strip leading zeroes


solution = Solution()
assert solution.toHex(26) == '1a'
assert solution.toHex(-1) == 'ffffffff'
