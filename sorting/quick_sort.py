def quick_sort_recursion(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    # Choose the first element as the pivot / reference point
    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort_recursion(left) + [pivot] + quick_sort_recursion(right)

# Time complexity is O(n log n) on average, O(n) × O(log n) = O(n log n)
# O(n^2) in the worst case, happens when pivot selects either the maximum or minimum value, = n(n+1)/2

def quick_sort(arr):
    # diverse partitioning strategy
    def partition(left, right):
        pivot = arr[right]  # Choose the last element as the pivot
        i = left - 1        # beginning of the partition, which is -1

        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                # Python supports assigning values to multiple variables simultaneously.
                # Java requires a temporary variable.

        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1

    # Recursive quicksort function
    def sort(left, right):
        if left < right:
            p = partition(left, right)
            sort(left, p - 1)
            sort(p + 1, right)

    sort(0, len(arr) - 1)
    return arr
