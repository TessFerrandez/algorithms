'''
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.
'''
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def lcp(s: str) -> List[str]:
            if len(s) == "":
                return []
            if len(s) == 1:
                if "a" <= s <= "z":
                    return[s, s.upper()]
                else:
                    return[s]

            permutations = []
            next_permutations = lcp(s[1:])

            if "a" <= s[0] <= "z":
                for permutation in next_permutations:
                    permutations.append(s[0] + permutation)
                    permutations.append(s[0].upper() + permutation)
            else:
                for permutation in next_permutations:
                    permutations.append(s[0] + permutation)

            return permutations

        return lcp(s.lower())


solution = Solution()
assert solution.letterCasePermutation("a1b2") == ['a1b2', 'A1b2', 'a1B2', 'A1B2']
assert solution.letterCasePermutation("3z4") == ['3z4', '3Z4']
