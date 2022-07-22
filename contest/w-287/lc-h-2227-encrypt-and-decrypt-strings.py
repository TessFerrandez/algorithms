from collections import defaultdict
from typing import List


# memory limit exceeded
class Encrypter1:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.lex = {}
        self.relex = defaultdict(list)

        for i in range(len(keys)):
            self.lex[keys[i]] = values[i]
            self.relex[values[i]].append(keys[i])

        self.dict = set(dictionary)

    def encrypt(self, word1: str) -> str:
        result = ''
        for ch in word1:
            result += self.lex[ch]
        return result

    def decrypt(self, word2: str) -> int:

        def get_strs(word):
            if len(word) == 2:
                return self.relex[word]
            else:
                possible = []
                first = word[:2]
                rest = get_strs(word[2:])
                for ch in self.relex[first]:
                    for w in rest:
                        possible.append(ch + w)
                return possible

        all_str = get_strs(word2)
        count = 0
        for s in all_str:
            if s in self.dict:
                count += 1
        return count


class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.lex = defaultdict(lambda: '#')
        for i in range(len(keys)):
            self.lex[keys[i]] = values[i]

        self.encrypted = defaultdict(int)
        for w in dictionary:
            self.encrypted[self.encrypt(w)] += 1

    def encrypt(self, word1: str) -> str:
        return ''.join(self.lex[ch] for ch in word1)

    def decrypt(self, word2: str) -> int:
        return self.encrypted[word2]


encrypter = Encrypter(['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"])
assert encrypter.encrypt('abcd') == 'eizfeiam'
assert encrypter.decrypt('eizfeiam') == 2
