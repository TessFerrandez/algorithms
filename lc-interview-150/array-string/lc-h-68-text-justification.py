# array, string , simulation
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lengths = [len(word) for word in words]

        row_total = 0
        row_words = []
        rows = []
        for length, word in zip(lengths, words):
            if row_total + 1 + length > maxWidth:
                rows.append(row_words)
                row_total = 0
                row_words = []
            if row_total == 0:
                row_total += length
                row_words = [word]
            elif row_total + 1 + length <= maxWidth:
                row_total += 1 + length
                row_words.append(word)

        rows.append(row_words)
        if rows[0] == []:
            rows.pop(0)

        space_rows = []
        for words in rows[:-1]:
            spaces = maxWidth - sum(len(word) for word in words)
            places_for_spaces = len(words) - 1
            if places_for_spaces > 0:
                spaces_per_place = spaces // places_for_spaces
                extra_spaces = spaces % places_for_spaces
                for i in range(len(words) - 1):
                    words[i] += " " * spaces_per_place
                    if extra_spaces > 0:
                        words[i] += " "
                        extra_spaces -= 1
            else:
                words[0] += " " * spaces

            space_rows.append("".join(words))

        space_rows.append(" ".join(rows[-1]) + " " * (maxWidth - len(" ".join(rows[-1]))))
        return space_rows


solution = Solution()
solution.fullJustify(["Listen","to","many,","speak","to","a","few."], 6)
assert solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) == ["This    is    an", "example  of text", "justification.  "]
assert solution.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16) == ["What   must   be", "acknowledgment  ", "shall be        "]
assert solution.fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20) == [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]