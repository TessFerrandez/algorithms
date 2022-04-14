def merge_sort(nums):
    '''
    merge sort requires <= 6n log2(n) + 6n operations => n * log n
    '''
    def merge(nums1, nums2):
        result = []
        n1 = len(nums1)
        n2 = len(nums2)
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        if i < n1:
            result += nums1[i:]
        else:
            result += nums2[j:]
        return result

    n = len(nums)

    if n <= 1:
        return nums

    left = merge_sort(nums[:n // 2])
    right = merge_sort(nums[n // 2:])
    return merge(left, right)


assert merge_sort([5, 4, 1, 8, 7, 2, 6, 3]) == [1, 2, 3, 4, 5, 6, 7, 8]
