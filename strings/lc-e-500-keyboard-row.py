from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = {0: "qwertyuiop" + "qwertyuiop".upper(), 1: "asdfghjkl" + "asdfghjkl".upper(), 2: "zxcvbnm" + "zxcvbnm".upper()}

        def find_row(word):
            for row in rows:
                if word[0] in rows[row]:
                    return row

        def match_row(word, row):
            for ch in word[1:]:
                if ch not in rows[row]:
                    return False
            return True

        result = []

        for word in words:
            row = find_row(word)
            if match_row(word, row):
                result.append(word)

        return result


solution = Solution()
assert solution.findWords(["Hello","Alaska","Dad","Peace"]) == ["Alaska","Dad"]
assert solution.findWords(["omk"]) == []
assert solution.findWords(["adsdf","sfd"]) == ["adsdf","sfd"]
