# Find fisrt bad version


def firstBadVersion(n):
        high = n
        low = 1
        mid = low + (high - low) // 2
        while low != high:
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
            mid = low + (high - low) // 2
        return mid
