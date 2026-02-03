def upperBound(arr: [int], x: int, n: int) -> int:
    left = 0
    right = n - 1
    ans = n   # default = n (if no upper bound)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > x:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans
