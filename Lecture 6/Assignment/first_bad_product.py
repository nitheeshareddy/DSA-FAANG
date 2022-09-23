#Time complexity: O(logn) - The search space is limited to half so the recurrence relation is T(n/2) + c
def find_bad_product_index(left, right, arr, target):
    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target and arr[mid - 1] != target :
            return mid
        elif arr[mid] < target :
            return find_bad_product_index(mid+1, right, arr, target)
        else:
            return find_bad_product_index(left, mid-1, arr, target)
    return -1


#driver code
arr = [0, 0, 0, 1, 1, 1, 1, 1, 1]
left = 0
right = len(arr) - 1
target = 1
result = find_bad_product_index(left, right, arr, target)
print(result)
