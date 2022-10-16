from typing import List
from collections import Counter


class Solution:
    # my solution
    def makePalindrome1(self, n: int, arr: List[str]) -> bool:
        words = Counter(arr)

        for word in arr:
            if word not in words:
                continue

            reversed = word[::-1]
            if reversed == word:
                # current="aba" remove even copies
                if words[word] % 2 == 0:
                    del words[word]
                else:
                    words[word] = 1
            else:
                if reversed not in words:
                    # current="abb" and "bba" is not in the list => return false
                    return False
                if words[reversed] != words[word]:
                    # current="abb" and "bba" is in the list - if they are the same count, remove them, else return false
                    return False
                del words[reversed]
                del words[word]

        if not words:
            return True
        if len(words) > 1:
            return False

        count = list(words.values())[0]
        word = list(words.keys())[0]

        if word == word[::-1] and count == 1:
            return True

        return False

    # suggested solution
    def makePalindrome2(self, n: int, arr: List[str]) -> bool:
        '''
        1. all strings have their reverse => true
        2. at max, one string does not have a reverse, but it is a palindrome => true
        3. all else => false
        '''
        def is_palindrome(word):
            return word == word[::-1]

        words = Counter(arr)
        num_reverse_absent = 0
        possible_palindrome = ""

        for word in arr:
            reversed = word[::-1]
            if words[reversed] != words[word]:
                num_reverse_absent += 1
                possible_palindrome = reversed

        if num_reverse_absent == 0:
            return True
        if num_reverse_absent > 1:
            return False
        return is_palindrome(possible_palindrome)

    # optimized - note that this (and the suggested solution) should fail for ["aba", "aba", "aba", "cdc", "cdc", "cdc"] but doesn't
    def makePalindrome(self, n: int, arr: List[str]) -> bool:
        words = Counter(arr)

        for word in arr:
            reversed = word[::-1]
            if words[reversed] != words[word]:
                return False

        return True


solution = Solution()
assert solution.makePalindrome(3, ["aba", "aba", "aba", "cdc", "cdc", "cdc"])
assert solution.makePalindrome(3, ["ghdas", "adsda", "sadhg"])
assert solution.makePalindrome(4, ["djfh", "gadt", "hfjd", "tdag"])
assert not solution.makePalindrome(3, ["jhjdf", "sftas", "fgsdf"])
assert not solution.makePalindrome(9, ["qjhpzpnsyp", "pysnpzphjq", "yrkkpohvaw", "wavhopkkry", "qgaeqzqwji", "ijwqzqeagq", "korsdogmqv", "vqmgodsrok", "pysnpzphjq"])
