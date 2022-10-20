from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words).most_common()
        word_counts.sort(key=lambda word: (-word[1], word[0]))
        return [word[0] for word in word_counts[:k]]


solution = Solution()
assert solution.topKFrequent(["i","love","leetcode","i","love","coding"], 2) == ["i","love"]
assert solution.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4) == ["the","is","sunny","day"]
