from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        out_of_place = [i for i in range(len(s)) if s[i] != goal[i]]
        if len(out_of_place) > 2:
            return False
        elif len(out_of_place) == 2:
            s_list = list(s)
            s_list[out_of_place[0]], s_list[out_of_place[1]] = s_list[out_of_place[1]], s_list[out_of_place[0]]
            if ''.join(s_list) == goal:
                return True
            return False
        elif len(out_of_place) == 0:
            counts = Counter(s)
            num_doubles = 0
            for ch in counts:
                if counts[ch] >= 2:
                    num_doubles += counts[ch] // 2
            if num_doubles >= 1:
                return True
        return False


solution = Solution()
solution.buddyStrings('ab', 'ba') == True
solution.buddyStrings('ab', 'ab') == False
solution.buddyStrings('aa', 'aa') == True
solution.buddyStrings('abac', 'abad') == False
