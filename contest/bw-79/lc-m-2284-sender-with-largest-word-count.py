from collections import defaultdict
from typing import List


class Solution:
    # my contest solution
    def largestWordCount1(self, messages: List[str], senders: List[str]) -> str:
        counts = defaultdict(int)

        max_count = 0
        best = ''

        for i in range(len(messages)):
            counts[senders[i]] += len(messages[i].split(' '))
            num_words = counts[senders[i]]
            if num_words >= max_count:
                if max_count == num_words:
                    best = senders[i] if senders[i] > best else best
                else:
                    max_count = num_words
                    best = senders[i]

        return best

    # simplified
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        word_count = defaultdict(int)

        for sender, message in zip(senders, messages):
            word_count[sender] += message.count(' ')

        return max([(count, sender) for sender, count in word_count.items()])[1]


solution = Solution()
assert solution.largestWordCount(["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders=["Alice","userTwo","userThree","Alice"]) == "Alice"
assert solution.largestWordCount(["How is leetcode for everyone","Leetcode is useful for practice"], senders=["Bob","Charlie"]) == "Charlie"
