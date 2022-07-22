from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = Counter(s)
        letters = sorted(counts.keys())

        result = ''
        while letters:
            letter = letters.pop()
            if letters and letters[-1] > letter:
                result += letter
                counts[letter] -= 1
                if counts[letter] > 0:
                    next_letter = letters.pop()
                    letters.append(letter)
                    letters.append(next_letter)
            elif counts[letter] > repeatLimit:
                result += letter * repeatLimit
                counts[letter] -= repeatLimit
                if letters:
                    next_letter = letters.pop()
                    letters.append(letter)
                    letters.append(next_letter)
            else:
                result += letter * counts[letter]
                counts[letter] = 0
        return result


solution = Solution()
assert solution.repeatLimitedString("xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1) == "zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba"
# zyxyxwxwvwvuvuvututst ststrqrqpqpopononmnmlmkjkigigif  ededededcbaba
# zyxyxwxwvwvuvuvututst rtrtqpqpqponononmlmkmk j igi  fi ededededcbaba
print(solution.repeatLimitedString('cczazcc', 3))
print(solution.repeatLimitedString('aababab', 2))
