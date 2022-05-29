class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(' ')
        for i, word in enumerate(words):
            if word.startswith('$') and word[1:].isnumeric():
                price = int(word[1:])
                new_price = price - price * discount / 100
                words[i] = f"${new_price:.2f}"
        return ' '.join(words)


solution = Solution()
assert solution.discountPrices("there are $1 $2 and 5$ candies in the shop", 50) == "there are $0.50 $1.00 and 5$ candies in the shop"
assert solution.discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100) == "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"
