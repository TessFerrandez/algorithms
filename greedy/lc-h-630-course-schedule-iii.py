from functools import cache
from heapq import heappop, heappush
from itertools import permutations
from typing import List


class Solution:
    # brute force - check all combinations
    def scheduleCourse1(self, courses: List[List[int]]) -> int:
        n = len(courses)

        max_courses = 0
        for permutation in permutations(range(n)):
            total_time, course_count = 0, 0

            for i in permutation:
                if total_time + courses[i][0] <= courses[i][1]:
                    total_time += courses[i][0]
                    course_count += 1
                else:
                    break
            max_courses = max(max_courses, course_count)

        return max_courses

    # memoization dp
    def scheduleCourse2(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])

        @cache
        def schedule(i, time):
            if i == len(courses):
                return 0
            taken = 0
            if time + courses[i][0] <= courses[i][1]:
                taken += 1 + schedule(i + 1, time + courses[i][0])
            not_taken = schedule(i + 1, time)
            return max(taken, not_taken)

        return schedule(0, 0)

    # iterative
    def scheduleCourse3(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        time, count = 0, 0

        for i in range(len(courses)):
            if time + courses[i][0] <= courses[i][1]:
                time += courses[i][0]
                count += 1
            else:
                max_i = i
                for j in range(i):
                    if courses[j][0] > courses[max_i][0]:
                        max_i = j
                if courses[max_i][0] > courses[i][0]:
                    time += courses[i][0] - courses[max_i][0]
                courses[max_i][0] = -1

        return count

    # optimized iterative
    def scheduleCourse4(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        time, count = 0, 0

        for i in range(len(courses)):
            if time + courses[i][0] <= courses[i][1]:
                time += courses[i][0]
                courses[count] = courses[i]
                count += 1
            else:
                max_i = i
                for j in range(i):
                    if courses[j][0] > courses[max_i][0]:
                        max_i = j
                if courses[max_i][0] > courses[i][0]:
                    time += courses[i][0] - courses[max_i][0]
                    courses[max_i] = courses[i]

        return count

    # extra array
    def scheduleCourse5(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        valid_list = []

        time = 0
        for course in courses:
            if time + course[0] < course[1]:
                valid_list.append(course[0])
                time += course[0]
            else:
                max_i = 0
                for i in range(1, len(valid_list)):
                    if valid_list[i] < valid_list[max_i]:
                        max_i = i
                if max_i < len(valid_list) and valid_list[max_i] > course[0]:
                    time += course[0] - valid_list[max_i]
                    valid_list[max_i] = course[0]
        return len(valid_list)

    # priority queue
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap, start = [], 0
        for duration, end in sorted(courses, key=lambda c: c[1]):
            start += duration
            heappush(heap, -duration)
            while start > end:
                start += heappop(heap)
        return len(heap)


solution = Solution()
assert solution.scheduleCourse([[100, 200],[200, 1300],[1000,1250],[2000,3200]]) == 3
assert solution.scheduleCourse([[1, 2]]) == 1
assert solution.scheduleCourse([[3, 2], [4, 3]]) == 0
