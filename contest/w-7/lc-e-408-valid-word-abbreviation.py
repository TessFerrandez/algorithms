class Solution:
    def validWordAbbreviation(self, word, abbr):
        i = j = 0
        abbr_len = len(abbr)
        word_len = len(word)

        count = 0
        while i < word_len and j < abbr_len:
            if '0' <= abbr[j] <= '9':
                count = count * 10 + int(abbr[j])
                j += 1
            elif count > 0:
                if i + count > word_len:
                    return False
                else:
                    i += count
                    count = 0
            else:
                if word[i] == abbr[j]:
                    i += 1
                    j += 1
                else:
                    return False

        return i + count == word_len and j == abbr_len


solution = Solution()
assert solution.validWordAbbreviation("apple", "a4")
assert not solution.validWordAbbreviation("internationalization", "i12iz4n")
assert not solution.validWordAbbreviation("apple", "a2e")
