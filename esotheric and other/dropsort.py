def drop_sort(numbers):
    result = []
    for number in numbers:
        if not result or number >= result[-1]:
            result.append(number)

    return result


print(drop_sort([1, 3, 3, 4, 1, 2, 1, 5]))  # [1, 3, 3, 4, 5]
