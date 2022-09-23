#Time complexity: O(logn) - The search space is limited to half so the recurrence relation is T(n/2) + c
#Space Complexity: O(1) - No extra space is used
def is_perfect_square(left, right, num):
    while left <= right:
        mid = left + (right - left)//2
        if mid * mid == num:
            return True
        elif mid*mid < num:
            return is_perfect_square(mid+1, right, num)
        else:
            return is_perfect_square(left, mid-1, num)
    return False      

#driver code
num = 16
left = 0
right = num
result = is_perfect_square(left, right, num)
print(result)
