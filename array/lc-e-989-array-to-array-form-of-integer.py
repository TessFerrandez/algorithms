from typing import List


class Solution:
    def addToArrayForm1(self, num: List[int], k: int) -> List[int]:
        number = 0
        num = num[::-1]
        while num:
            number *= 10
            number += num.pop()

        total = number + k
        return [int(d) for d in str(total)]

    def addToArrayForm2(self, num: List[int], k: int) -> List[int]:
        return list(map(int, list(str(int(''.join(map(str, num))) + k))))

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num2 = [int(d) for d in str(k)]
        result = []
        carry = 0
        while num or num2:
            n1 = num.pop() if num else 0
            n2 = num2.pop() if num2 else 0
            res = n1 + n2 + carry
            carry = res // 10
            result.append(res % 10)
        if carry:
            result.append(carry)
        return result[::-1]


solution = Solution()
assert solution.addToArrayForm([1, 2, 0, 0], 34) == [1, 2, 3, 4]
assert solution.addToArrayForm([2, 7, 4], 181) == [4, 5, 5]
assert solution.addToArrayForm([2, 1, 5], 806) == [1, 0, 2, 1]
