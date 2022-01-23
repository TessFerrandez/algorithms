'''
You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:

If the length of the word is 1 or 2 letters, change all letters to lowercase.
Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title
'''
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        result = ""
        for word in words:
            if len(word) < 3:
                result += " " + word.lower()
            else:
                result += " " + word.capitalize()
        return result.strip()


solution = Solution()
assert solution.capitalizeTitle("capiTalIze tHe titLe") == "Capitalize The Title"
assert solution.capitalizeTitle("First leTTeR of EACH Word") == "First Letter of Each Word"
assert solution.capitalizeTitle("i lOve leetcode") == "i Love Leetcode"