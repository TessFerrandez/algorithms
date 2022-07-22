from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = set()
        adjacent = defaultdict(list)

        def dfs(merged_account, email):
            visited.add(email)
            merged_account.append(email)

            if email not in adjacent:
                return

            for neighbor in adjacent[email]:
                if neighbor not in visited:
                    dfs(merged_account, neighbor)

        for account in accounts:
            account_first_email = account[1]

            for j in range(2, len(account)):
                account_email = account[j]
                adjacent[account_first_email].append(account_email)
                adjacent[account_email].append(account_first_email)

        merged_accounts = []
        for account in accounts:
            account_name, account_first_email = account[0], account[1]

            # if email is visited, then it is part of a different component
            if account_first_email not in visited:
                merged_account = [account_name]
                dfs(merged_account, account_first_email)
                merged_account = [merged_account[0]] + list(sorted(merged_account[1:]))
                merged_accounts.append(merged_account)
        return merged_accounts


solution = Solution()
assert solution.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]) == [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
assert solution.accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]) == [['Gabe', 'Gabe0@m.co', 'Gabe1@m.co', 'Gabe3@m.co'], ['Kevin', 'Kevin0@m.co', 'Kevin3@m.co', 'Kevin5@m.co'], ['Ethan', 'Ethan0@m.co', 'Ethan4@m.co', 'Ethan5@m.co'], ['Hanzo', 'Hanzo0@m.co', 'Hanzo1@m.co', 'Hanzo3@m.co'], ['Fern', 'Fern0@m.co', 'Fern1@m.co', 'Fern5@m.co']]
