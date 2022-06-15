from collections import defaultdict
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            domain_parts = domain.split('.')
            for i in range(len(domain_parts)):
                dom = '.'.join(domain_parts[i:])
                domains[dom] += int(count)

        results = [str(count) + " " + domain for domain, count in domains.items()]
        return results

solution = Solution()
assert solution.subdomainVisits(["9001 discuss.leetcode.com"]) == ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
assert solution.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]) == ["900 google.mail.com", "901 mail.com", "951 com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org", "5 org"]
