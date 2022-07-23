class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(' ')
        new_title = ""
        for word in words:
            if len(word) <= 2:
                new_title += word.lower() + " "
            else:
                new_title += word.title() + " "
        new_title = new_title.strip()
        return new_title


solution = Solution()
assert solution.capitalizeTitle("capiTalIze tHe titLe") == "Capitalize The Title"
assert solution.capitalizeTitle("First leTTeR of EACH Word") == "First Letter of Each Word"
assert solution.capitalizeTitle("i lOve leetcode") == "i Love Leetcode"
