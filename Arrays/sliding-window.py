def longest_substring(s: str) -> int: 
    """
    Length of longest substring of 1's
    """
    n = len(s) 
    left = ans = 0 

    for right in range(n): 
        if s[right] == "0":
            ans = max(ans, right - left)
            left = right + 1
    
    return ans 
         
s = "100111001"
# print(longest_substring(s))


def flip_once(s: str) -> int:
    """
    You may flip one 0. What is the length of the longest substring containing only 1's? 
    """

    n = len(s)
    left = ans = zeros = 0

    for right in range(n): 
        if s[right] == "0":
            zeros += 1
        while zeros > 1:
            if s[left] == "0":
                zeros -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans 

# print(flip_once(s))


def subarray_prod_lessthan(nums, k) -> int:
    """
    number of subarrays where product of elements strictly less than k 
    """
    if k <= 1: 
        return 0

    n = len(nums) 
    ans = left = 0
    curr = 1 

    for right in range(n): 
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1

        ans += right - left + 1  # adding size of window because they are all valid subarrays!
        
    return ans

# nums = [10, 5, 2, 6]
# print(subarray_prod_lessthan(nums, 100))


def largest_subarray_sum_bad(nums, k) -> int: 
    """
    largest sum of subarray with length k
    """
    n = len(nums)
    ans = left = 0 

    for left in range(n - k):
        right = left + k
        curr = sum(nums[left:right])
        ans = max(ans, curr)

    return ans


def largest_subarray_sum_good(nums, k) -> int: 
    """
    largest sum of subarray with length k
    """
    n = len(nums)
    left = ans = 0 

    # sum of first k elements
    for i in range(k):
        ans += nums[i]
    
    # move window by one position 
    curr = ans 
    right = k
    while right < n:
        left += 1
        curr += nums[right] - nums[left]
        right += 1
        ans = max(ans, curr)

    return ans

# nums = [3, -1, 4, 12, -8, 5, 6]
# print(largest_subarray_sum_bad(nums, 4))
# print(largest_subarray_sum_good(nums, 4))


def max_subarray_avg(nums, k) -> float: 
    n = len(nums)
    ans = curr = 0 

    # build first k-element window
    for i in range(k): 
        curr += nums[i]
    ans = curr  
    ans /= k

    left, right = 0, k

    while right < n:
        curr += nums[right] - nums[left]
        ans = max(ans, curr/k)
        left += 1
        right += 1
        
    return ans 

# nums = [1,12,-5,-6,50,3,9]
# nums = [5]
# k = 1
# print(max_subarray_avg(nums, k))


def max_cons_ones(nums, k) -> int:
    """
    flip at most k 0's 
    """
    n = len(nums) 
    left = ans = zeros = 0 

    for right in range(n): 
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans 


nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(max_cons_ones(nums, k))

