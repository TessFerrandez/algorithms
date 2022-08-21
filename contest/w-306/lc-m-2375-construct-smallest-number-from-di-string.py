class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = [1]
        insert_at = 0
        next_num = 2

        for i, p in enumerate(pattern):
            if p == 'I':
                result.append(next_num)
                insert_at = i + 1
            else:
                result = result[: insert_at] + [next_num] + result[insert_at:]
            next_num += 1
        return ''.join([str(d) for d in result])


solution = Solution()
assert solution.smallestNumber('IIIDIDDD') == "123549876"
assert solution.smallestNumber('DDD') == "4321"
