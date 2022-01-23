'''
There are two types of persons:

The good person: The person who always tells the truth.
The bad person: The person who might tell the truth and might lie.
You are given a 0-indexed 2D integer array statements of size n x n that represents the statements made by n people about each other. More specifically, statements[i][j] could be one of the following:

0 which represents a statement made by person i that person j is a bad person.
1 which represents a statement made by person i that person j is a good person.
2 represents that no statement is made by person i about person j.
Additionally, no person ever makes a statement about themselves. Formally, we have that statements[i][i] = 2 for all 0 <= i < n.

Return the maximum number of people who can be good based on the statements made by the n people.
'''
from typing import List


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n_people = len(statements)

        def is_valid(state):
            for i in range(n_people):
                # for all people
                # if the person is good - check that his answers are always true
                if state[i] == "1":
                    for j in range(n_people):
                        if statements[i][j] != 2 and statements[i][j] != int(state[j]):
                            return False
            return True

        max_good = 0

        # loop through all possible combos of good and bad Ex. 2 people 00, 01, 10, 11
        for i in range(2 ** n_people):
            state = bin(i)[2:].zfill(n_people)
            if is_valid(state):
                # if it was a valid state -- check how many good people we had
                max_good = max(max_good, state.count('1'))

        return max_good


solution = Solution()
assert solution.maximumGood([[2,1,2],[1,2,2],[2,0,2]]) == 2
assert solution.maximumGood([[2,0],[0,2]]) == 1
