class Solution:
    # brute force
    def countVowelSubstrings(self, word: str) -> int:
        substrings, n = 0, len(word)

        for i in range(n):
            vowels = set()
            j = i
            while j < n and word[j] in 'aeiou':
                vowels.add(word[j])
                if len(vowels) == 5:
                    substrings += 1
                j += 1
        return substrings

    # sliding window
    def countVowelSubstrings1(self, word: str) -> int:
        '''
        S = start, L = left, R = right/current
          SL    R
        xxaiioueiiaxx   1
          SL     R
        xxaiioueiiaxx   1
          S   L   R
        xxaiioueiiaxx   4

        S = marks the start of an all-wovel substring
        R = right/current position
        The window between Left - 1 and Right is the smallest window
        with all 5 vowels
        '''
        counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        sub_strings, vowels = 0, 0
        start, left = 0, 0

        for right, ch in enumerate(word):
            # we got a vowel
            if ch in counts:
                counts[ch] += 1

                # found a new vowel
                if counts[ch] == 1:
                    vowels += 1

                # shrink form left while we still have 5 vowels
                while vowels == 5:
                    counts[word[left]] -= 1
                    if counts[word[left]] == 0:
                        vowels -= 1
                    left += 1

                # count the sub_strings we found
                sub_strings += left - start

            # no vowel - reset all
            else:
                counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
                vowels = 0
                start = left = right + 1

        return sub_strings


solution = Solution()
assert solution.countVowelSubstrings("aeiouu") == 2
assert solution.countVowelSubstrings("unicornarihan") == 0
assert solution.countVowelSubstrings("cuaieuouac") == 7
