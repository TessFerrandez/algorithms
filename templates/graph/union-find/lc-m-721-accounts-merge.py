from collections import defaultdict
from typing import List
from UnionFind import UnionFind


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        all_accounts = defaultdict(list)
        for account in accounts:
            name = account[0]
            emails = account[1:]
            all_accounts[name].append(emails)

        merged = []
        for name in all_accounts:
            if len(all_accounts[name]) == 1:
                merged.append([name] + sorted(set(all_accounts[name][0])))
            else:
                emails = set()
                for email_group in all_accounts[name]:
                    for email in email_group:
                        emails.add(email)
                uf = UnionFind(emails)
                for email_group in all_accounts[name]:
                    for i in range(len(email_group)):
                        for j in range(i + 1, len(email_group)):
                            uf.union(email_group[i], email_group[j])
                groups = defaultdict(set)
                for email in emails:
                    groups[uf.find(email)].add(email)
                for group in groups:
                    merged.append([name] + sorted(list(groups[group])))

        return merged


solution = Solution()
print(solution.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
print(solution.accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))
