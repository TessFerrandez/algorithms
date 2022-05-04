def is_invalid():
    # check if state is invalid
    pass

def find_max_window(nums):
    n = len(nums)
    result, left = 0, 0

    for right in range(n):
        # update state by adding "right"
        # this might make the window invalid
        while is_invalid():
            # update state by removing "left"
            left += 1
        result = max(result, right - left + 1)

    return result


def find_max_window2(nums):
    n = len(nums)
    result, left = 0, 0

    for right in range(n):
        # update state in A[j] that might make the window invalid
        if is_invalid():                            # shrink window from left until state is valid
            # update state using A[i]
            left += 1
        result = max(result, right - left + 1)      # window[left, right] is the maximum so far

    return result
