'''
You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.
'''
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0

        for ch in s:
            if ch == 'L':
                late += 1
                if late == 3:
                    return False
            else:
                late = 0
                if ch == 'A':
                    absent += 1
                    if absent == 2:
                        return False

        return True


solution = Solution()
assert solution.checkRecord('PPALLP')
assert solution.checkRecord('PPALLL')
assert not solution.checkRecord('PPALLAP')
