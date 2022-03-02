'''
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(num) for num in version1.split('.')]
        v2 = [int(num) for num in version2.split('.')]

        v1_len = len(v1)
        v2_len = len(v2)
        max_len = max(v1_len, v2_len)

        for i in range(max_len):
            v1num = v1[i] if v1_len > i else 0
            v2num = v2[i] if v2_len > i else 0

            if v1num > v2num:
                return 1
            if v2num > v1num:
                return -1

        return 0


solution = Solution()
assert solution.compareVersion('0.1', '1.1') == -1
assert solution.compareVersion('1.01', '1.001') == 0
assert solution.compareVersion('1.0', '1.0.0') == 0
assert solution.compareVersion('1.1', '0.1') == 1
