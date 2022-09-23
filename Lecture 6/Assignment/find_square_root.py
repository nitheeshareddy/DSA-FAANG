#Time complexity: O(logn) - The search space is limited to half so the recurrence relation is T(n/2) + c

def sqrt(num):
    right =num
    left= 0
    while (left <= right):
        mid= left + (right - left)//2  
        if mid*mid<= num :
            left= mid+1  
        else:
            right= mid -1   
    return left - 1
# Driver Code
num= 10
print(sqrt(num))
