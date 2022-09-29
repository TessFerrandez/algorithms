from heapq import heappop, heappush


class Solution:
    def minAbbreviation(self, target, dictionary):
        target_len = len(target)

        if len(dictionary) == 0:
            return str(target_len)

        q = []

        def get_abbr_len(abbr):
            ''' ex a32bc has len 4 '''
            count = 0
            prev_is_num = False

            for ch in abbr:
                if '0' <= ch <= '9':
                    if not prev_is_num:
                        count += 1
                        prev_is_num = True
                else:
                    prev_is_num = False
                    count += 1

            return count

        # using dfs
        def find_abbreviations(prefix, start):
            new_abbr = prefix + target[start:]
            heappush(q, (get_abbr_len(new_abbr), new_abbr))

            if start == target_len:
                return

            i = start + 1 if start > 0 else 0

            while i < target_len:
                next = prefix + target[start: i]

                for j in range(1, target_len):
                    find_abbreviations(next + str(j), i + j)

                i += 1

        def is_match(abbr, s):
            i = j = count = 0
            abbr_len, s_len = len(abbr), len(s)

            while i < abbr_len and j < s_len:
                if '0' <= abbr[i] <= '9':
                    count = count * 10 + int(abbr[i])
                else:
                    j += count
                    count = 0

                    if j >= s_len or abbr[i] != s[j]:
                        return False

                    j += 1
                i += 1

            return i == abbr_len and j + count == s_len

        find_abbreviations(prefix="", start=0)

        while q:
            _, abbreviation = heappop(q)
            found_match = False

            for word in dictionary:
                if is_match(abbreviation, word):
                    found_match = True
                    break

            if not found_match:
                return abbreviation

        return ""


solution = Solution()
assert solution.minAbbreviation("apple", ["blade"]) == "a4"
assert solution.minAbbreviation("apple", ["plain", "amber", "blade"]) == "1p3"
