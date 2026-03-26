def lowerBound(arr, target):
    n = len(arr)
    st, end = 0, n - 1
    ans = n

    while st <= end:
        mid = st + (end - st) // 2

        if arr[mid] >= target:
            ans = mid
            end = mid - 1
        else:
            st = mid + 1

    return ans
