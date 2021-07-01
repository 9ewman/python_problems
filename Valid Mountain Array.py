# Given an array of integers arr, return true if and only if it is a valid mountain array.


def validMountainArray(arr) -> bool:
    n = len(arr)
    if n < 3:
        return False
    if arr[0] >= arr[1]:
        return False
    increasing = True
    for i in range(1, n - 1):
        if increasing:
            if arr[i] > arr[i + 1]:
                increasing = False
            elif arr[i] == arr[i + 1]:
                return False
        else:
            if arr[i] <= arr[i + 1]:
                return False
    if increasing:
        return False
    return True
