from typing import List


class Solution:
    def kthPalindrome1(self, queries: List[int], intLength: int) -> List[int]:
        def get_inner(n, ilen):
            if ilen == 1:
                return str(n)
            if ilen == 2:
                return str(n) * 2

            if ilen % 2 == 0:
                ifactor = 10 ** ((ilen - 1) // 2)
            else:
                ifactor = 10 ** ((ilen) // 2)

            outer = n // ifactor
            inner = n % ifactor

            return str(outer) + get_inner(inner, ilen - 2) + str(outer)

        if intLength % 2 == 0:
            factor = 10 ** ((intLength - 1) // 2)
        else:
            factor = 10 ** ((intLength) // 2)

        max_n = 9 * factor

        result = []
        for query in queries:
            if query > max_n:
                result.append(-1)
            elif intLength == 1:
                result.append(query)
            elif intLength == 2:
                result.append(int(str(query) * 2))
            else:
                outer = ((query - 1) // factor) + 1
                inner = (query - 1) % factor
                result.append(int(str(outer) + get_inner(inner, intLength - 2) + str(outer)))

        return result

    def kthPalindrome(self, queries: List[int], sz: int) -> List[int]:
        '''
        ex.
        1   10|01
        2   11|11
        ...
        90  99|99

        q + 10 - 1

        1   100|01
        2   101|01
        ...
        900 999|99

        q + 100 - 1

        then add the reverse
        '''
        base = 10 ** ((sz - 1) // 2)
        answers = [query - 1 + base for query in queries]

        for i, answer in enumerate(answers):
            answer = str(answer) + str(answer)[-1 - sz % 2:: -1]
            answers[i] = int(answer) if len(answer) == sz else -1

        return answers


solution = Solution()
assert solution.kthPalindrome([2, 4, 6], 4) == [1111, 1331, 1551]
assert solution.kthPalindrome([696771750,62,47,14,17,192356691,209793716,23,220935614,447911113,5,4,72], 4) == [-1, 7117, 5665, 2332, 2662, -1, -1, 3223, -1, -1, 1441, 1331, 8118]
assert solution.kthPalindrome([2,201429812,8,520498110,492711727,339882032,462074369,9,7,6], 1) == [2, -1, 8, -1, -1, -1, -1, 9, 7, 6]
assert solution.kthPalindrome([100, 900], 5) == [19991, 99999]
assert solution.kthPalindrome([1, 2, 3, 4, 5, 90], 3) == [101, 111, 121, 131, 141, 999]
