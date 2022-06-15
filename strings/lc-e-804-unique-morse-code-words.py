from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()

        for word in words:
            transformation = ''
            for ch in word:
                transformation += alphabet[ord(ch) - ord('a')]
            transformations.add(transformation)

        return len(transformations)


solution = Solution()
assert solution.uniqueMorseRepresentations(["gin","zen","gig","msg"]) == 2
assert solution.uniqueMorseRepresentations(["a"]) == 1
