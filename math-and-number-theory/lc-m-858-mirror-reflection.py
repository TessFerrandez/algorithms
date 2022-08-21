class Solution:
    def mirrorReflection1(self, p: int, q: int) -> int:
        current = q
        diff = q

        right = True
        while current != 0 and current != p:
            if 0 <= current + diff <= p:
                current += diff
            elif diff > 0:
                current = p - (current + diff - p)
                diff = - diff
            else:
                current = 0 - (current + diff)
                diff = -diff

            right = not right

        if current == 0:
            return 0
        if right:
            return 1
        return 2

    # optimal - https://leetcode.com/problems/mirror-reflection/discuss/2376191/C%2B%2B-Java-Python-or-Faster-then-100-or-Full-explanations-or
    def mirrorReflection(self, p: int, q: int) -> int:
        '''
        find m * p = n * q
        m = room extensions + 1
        n = light reflections + 1

        if light reflections are odd (n is even):
            we are in corner 2
        else if room extensions are even (m is odd):
            we are in corner 1
        else:
            we are in corner 0
        '''
        m, n = q, p
        m_is_even = m % 2 == 0
        n_is_even = n % 2 == 0

        while m_is_even and n_is_even:
            m //= 2
            n //= 2

        if n_is_even:
            return 2
        elif m_is_even:
            return 0
        else:
            return 1


solution = Solution()
assert solution.mirrorReflection(2, 1) == 2
assert solution.mirrorReflection(3, 1) == 1
assert solution.mirrorReflection(3, 2) == 0
assert solution.mirrorReflection(5, 2) == 0
assert solution.mirrorReflection(4, 3) == 2
