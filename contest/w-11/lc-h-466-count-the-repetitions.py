class Solution:
    def getMaxRepetitions1(self, s1: str, n1: int, s2: str, n2: int) -> int:
        count = index = 0
        counts, indices = [], []

        for i in range(n1):
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        count += 1
                        index = 0

            counts.append(count)
            indices.append(index)

            for ii in range(i):
                if indices[ii] == index:
                    prev = counts[ii]
                    repeat = (count - prev) * ((n1 - 1 - ii) // (i - ii))
                    post = counts[ii + (n1 - 1 - ii) % (i - ii)] - counts[ii]
                    return (prev + repeat + post) // n2

        return counts[-1] // n2

    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        pattern = {}
        s1_len, s2_len = len(s1), len(s2)
        str1_len, str2_len = s1_len * n1, s2_len * n2
        virtual_s1_idx = virtual_s2_idx = 0

        while virtual_s1_idx < str1_len:
            s1_idx, s2_idx = virtual_s1_idx % s1_len, virtual_s2_idx % s2_len
            if s1[s1_idx] == s2[s2_idx]:
                if (s1_idx, s2_idx) in pattern:
                    prev_s1_idx, prev_s2_idx = pattern[((s1_idx, s2_idx))]
                    s1_cycle_len = virtual_s1_idx - prev_s1_idx
                    s2_cycle_len = virtual_s2_idx - prev_s2_idx
                    cycle_count = (str1_len - virtual_s1_idx) // s1_cycle_len
                    virtual_s1_idx += cycle_count * s1_cycle_len
                    virtual_s2_idx += cycle_count * s2_cycle_len
                    if virtual_s1_idx >= str1_len:
                        break
                else:
                    pattern[(s1_idx, s1_idx)] = [virtual_s1_idx, virtual_s2_idx]
                virtual_s2_idx += 1
            virtual_s1_idx += 1

        return virtual_s2_idx // str2_len


solution = Solution()
assert solution.getMaxRepetitions('abc', 4, 'ab', 2) == 2
assert solution.getMaxRepetitions('abc', 1, 'abc', 1) == 1
