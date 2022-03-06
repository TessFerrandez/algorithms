'''
You are given a string s consisting only of lowercase English letters.

In one move, you can select any two adjacent characters of s and swap them.

Return the minimum number of moves needed to make s a palindrome.

Note that the input will be generated such that s can always be converted to a palindrome.
'''
class Solution:
    # wrong for eqvvhtcsaaqtqesvvqch
    def minMovesToMakePalindrome2(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return 0
        if s[0] == s[n - 1]:
            return self.minMovesToMakePalindrome(s[1:-1])

        from_right = 0
        from_left = 0
        for i in range(n):
            if s[i] == s[n - 1]:
                from_left = i
                break
        for i in range(n - 1, -1, -1):
            if s[i] == s[0]:
                from_right = i
                break

        if from_left <= n - from_right:
            # swap
            s = s[from_left] + s[:from_left] + s[from_left + 1:]
            return from_left + self.minMovesToMakePalindrome(s[1: -1])
        else:
            # swap right
            pass
            s = s[:from_right] + s[from_right + 1:] + s[from_right]
            return from_left + self.minMovesToMakePalindrome(s[1: -1])

    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        min_moves = 0
        left, right = 0, len(s) - 1

        while right > left:
            if s[left] != s[right]:
                i = right
                while i > left and s[i] != s[left]:
                    i -= 1
                if i == left:
                    s[left], s[left + 1] = s[left + 1], s[left]
                    min_moves += 1
                else:
                    while i < right:
                        s[i], s[i + 1] = s[i + 1], s[i]
                        min_moves += 1
                        i += 1
                    left += 1
                    right -= 1
            else:
                left += 1
                right -= 1

        return min_moves


solution = Solution()
assert solution.minMovesToMakePalindrome("eqvvhtcsaaqtqesvvqch") == 17
assert solution.minMovesToMakePalindrome('aabb') == 2
assert solution.minMovesToMakePalindrome('letelt') == 2
