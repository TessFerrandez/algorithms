class Solution:
    def largestVariance(self, s: str) -> int:
        '''
        Find the highest diff for each pair of characters
        '''
        result = 0
        chars = list(set(s))

        for i in range(len(chars)):
            for j in range(i + 1, len(chars)):
                ch1, ch2 = chars[i], chars[j]

                diff = 0
                max_diff = min_diff = 0
                last_ch1_diff = last_ch2_diff = 0

                found_ch1 = found_ch2 = False

                for c in s:
                    if c == ch1:
                        found_ch1 = True
                        diff += 1
                        max_diff = max(last_ch1_diff, max_diff)
                        last_ch1_diff = diff
                    elif c == ch2:
                        found_ch2 = True
                        diff -= 1
                        min_diff = min(last_ch2_diff, min_diff)
                        last_ch2_diff = diff
                    else:
                        continue

                    if found_ch1 and found_ch2:
                        result = max(diff - min_diff, max_diff - diff, result)
        return result


solution = Solution()
assert solution.largestVariance('aababbb') == 3
assert solution.largestVariance('abcde') == 0
assert solution.largestVariance("aabbbbaa") == 3
