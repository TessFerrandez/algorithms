def binary_search(low, high):
    def is_valid(value):
        return True

    while low < high:
        mid = low + (high - low) // 2
        if is_valid(mid):
            high = mid
        else:
            low = mid + 1

    return low
