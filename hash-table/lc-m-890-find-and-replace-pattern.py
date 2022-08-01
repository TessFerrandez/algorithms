from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            ch_map = {}
            visited = set()
            for w, p in zip(word, pattern):
                if w in ch_map:
                    if ch_map[w] == p:
                        continue
                    else:
                        return False
                else:
                    if p in visited:
                        return False
                    else:
                        ch_map[w] = p
                        visited.add(p)
            return True

        return list(filter(match, words))


solution = Solution()
assert solution.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], 'abb') == ['mee', 'aqq']
