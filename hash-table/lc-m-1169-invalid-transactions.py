from typing import List
from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # invalid if
        # amount exceeds 1000
        # occurs within (and including) 60 mins of another transaction with the same name in a different city
        transaction_map = defaultdict(list)
        bad_transactions = []

        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time, amount = int(time), int(amount)
            transaction_map[name].append((time, amount, city))

        for name in transaction_map:
            for time, amount, city in transaction_map[name]:
                current_bad = False

                if amount > 1000:
                    current_bad = True

                for ptime, pamount, pcity in transaction_map[name]:
                    if abs(ptime - time) <= 60 and pcity != city:
                        current_bad = True

                if current_bad:
                    bad_transactions.append(f"{name},{time},{amount},{city}")

        return bad_transactions


solution = Solution()
assert solution.invalidTransactions(["alice,20,1220,mtv","alice,20,1220,mtv"]) == ["alice,20,1220,mtv","alice,20,1220,mtv"]
assert solution.invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]) == ["alice,20,800,mtv","alice,50,100,beijing"]
assert solution.invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"]) == ["alice,50,1200,mtv"]
assert solution.invalidTransactions(["alice,20,800,mtv","bob,50,1200,mtv"]) == ["bob,50,1200,mtv"]
