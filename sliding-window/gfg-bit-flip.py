'''
Maximize number of 0s by flipping a subarray
'''

# simple O(n^2) - Kadane - consider all subarrays and
# find a subarray with (max count 1) - (max count 0)
def bit_flip1(arr):
    max_diff = 0
    orig_zero_count = 0
    n = len(arr)

    for i in range(n):
        if arr[i] == 0:
            orig_zero_count += 1

        count1, count0 = 0, 0

        for j in range(i, n):
            if arr[j] == 1:
                count1 += 1
            else:
                count0 += 1
            max_diff = max(max_diff, count1 - count0)

    return orig_zero_count + max_diff

# O(n) - based on largest sub array sum problem
# counting 0s as -1 and 1s as 1
def bit_flip(arr):
    max_diff = 0
    orig_zero_count = 0
    curr_max = 0

    for num in arr:
        if num == 0:
            orig_zero_count += 1

        diff = 1 if num == 1 else -1
        curr_max = max(diff, curr_max + diff)
        max_diff = max(max_diff, curr_max)
        print(curr_max, max_diff)

    print(orig_zero_count + max_diff)
    return orig_zero_count + max_diff


assert bit_flip([0, 1, 0, 0, 1, 1, 0]) == 6
assert bit_flip([0, 0, 0, 1, 0, 1]) == 5
assert bit_flip([0, 1, 1, 0, 1, 1]) == 5
