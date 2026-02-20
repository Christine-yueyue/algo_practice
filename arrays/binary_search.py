# finds the position of a target value in a sorted array by repeatedly dividing the search interval in half.

# time complexity is O(log n) 

def binary_search_basic(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# better version that can handle both ascending and descending sorted arrays
def binary_search(arr, target):
    
    if not arr:
        return -1
    
    low = 0
    high = len(arr) - 1
    ascending = arr[low] < arr[high]  # 1，2，3，4

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if ascending:
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if arr[mid] > target:
                low = mid + 1
            else:
                high = mid - 1

    return -1


# 01
# In Java, (low + high) may overflow if both values are large integers.
# To prevent overflow, we compute mid as low + (high - low) / 2.
# However, in Python, integers can grow arbitrarily large 任意精度, so we don't have to worry about overflow 整数溢出.