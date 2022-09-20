from collections import defaultdict


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        arriveAlice = [int(d) for d in arriveAlice.split('-')]
        leaveAlice = [int(d) for d in leaveAlice.split('-')]
        arriveBob = [int(d) for d in arriveBob.split('-')]
        leaveBob = [int(d) for d in leaveBob.split('-')]

        def generate_days(arrive_month, arrive_day, leave_month, leave_day):
            days = defaultdict(set)

            if arrive_month == leave_month:
                for day in range(arrive_day, leave_day + 1):
                    days[arrive_month].add(day)
            else:
                for day in range(arrive_day, days_in_month[arrive_month - 1] + 1):
                    days[arrive_month].add(day)
                for month in range(arrive_month + 1, leave_month):
                    for day in range(1, days_in_month[month - 1] + 1):
                        days[month].add(day)
                for day in range(1, leave_day + 1):
                    days[leave_month].add(day)

            return days

        alice = generate_days(arriveAlice[0], arriveAlice[1], leaveAlice[0], leaveAlice[1])
        bob = generate_days(arriveBob[0], arriveBob[1], leaveBob[0], leaveBob[1])

        count = 0
        for month in bob:
            count += len(bob[month].intersection(alice[month]))

        return count


solution = Solution()
assert solution.countDaysTogether("08-06", "12-08", "02-04", "09-01") == 27
assert solution.countDaysTogether("09-01", "10-19", "06-19", "10-20") == 49
assert solution.countDaysTogether("08-15", "08-18", "08-16", "08-19") == 3
assert solution.countDaysTogether("10-01", "10-31", "11-01", "12-31") == 0
