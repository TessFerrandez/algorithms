class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(1 for i in range(len(guess)) if secret[i] == guess[i])
        both = sum(min(secret.count(num), guess.count(num)) for num in set(guess))
        cows = both - bulls
        return f'{bulls}A{cows}B'


solution = Solution()
assert solution.getHint("1807", "7810") == "1A3B"
assert solution.getHint("1123", "0111") == "1A1B"
