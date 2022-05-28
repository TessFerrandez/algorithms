'''
Choices to make:
1. How to initialize low/high
    - they should include all possible values
2. Should you return low or (low - 1)
    - remember after exiting, low is the minimal k that satisfies the is_valid function
3. Design the "is_valid" function
'''
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
