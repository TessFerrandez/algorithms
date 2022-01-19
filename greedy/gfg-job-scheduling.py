'''
https://www.geeksforgeeks.org/job-sequencing-problem/
'''
def schedule_jobs1(jobs, t):
    n = len(jobs)

    # sort jobs according
    # to decreasing order of profit
    jobs.sort(key=lambda k: k[2])
    jobs = jobs[::-1]

    # keep track of free time-slots
    # and scheduled jobs
    free = [False] * t
    scheduled = ['-1'] * t

    for i in range(len(jobs)):
        for j in range(min(t - 1, jobs[i][1] - 1), -1, -1):
            if not free[j]:
                free[j] = True
                scheduled[j] = jobs[i][0]
                break

    return scheduled


# O(n2)
def schedule_jobs(jobs, t):
    scheduled = []

    # sort jobs
    jobs.sort(key=lambda k: k[2])
    jobs.reverse()

    while t > 0:
        for job in jobs:
            if job[1] >= t:
                scheduled.append(job[0])
                jobs.remove(job)
                t -= 1
                break

    scheduled.reverse()
    return scheduled


#    name deadline profit
jobs = [['a', 2, 100],
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15]]

scheduled = schedule_jobs(jobs, 3)
print(scheduled)
