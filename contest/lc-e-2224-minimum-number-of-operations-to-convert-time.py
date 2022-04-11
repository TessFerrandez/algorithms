class Solution:
    # my solution
    def convertTime1(self, current: str, correct: str) -> int:
        hr, min = current.split(':')
        hr, min = int(hr), int(min)

        hr2, min2 = correct.split(':')
        hr2, min2 = int(hr2), int(min2)

        min_diff = min2 - min

        count = 0
        hr_rest = 0

        if min_diff < 0:
            min_diff += 60
            hr_rest -= 1

        num_15 = min_diff // 15
        min_diff -= (num_15 * 15)
        count += num_15
        num_5 = min_diff // 5
        min_diff -= (num_5 * 5)
        count += num_5
        count += min_diff

        hr2 += hr_rest
        if hr2 < hr:
            hr2 += 24
        count += hr2 - hr
        return count

    # cleaner
    def convertTime(self, current: str, correct: str) -> int:
        current_time = 60 * int(current[: 2]) + int(current[3: 5])
        target_time = 60 * int(correct[: 2]) + int(correct[3: 5])
        diff = target_time - current_time
        count = 0

        for i in [60, 15, 5, 1]:
            count += diff // i
            diff %= i

        return count


solution = Solution()
assert solution.convertTime(current="09:41", correct="10:34") == 7
assert solution.convertTime(current="00:00", correct="23:59") == 32
assert solution.convertTime(current="02:30", correct="04:35") == 3
assert solution.convertTime("11:00", correct="11:01") == 1
