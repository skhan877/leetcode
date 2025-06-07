def prefix_sum(nums): 
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    return prefix

# nums = [5, 2, 1, 6, 3, 8]
# print(prefix_sum(nums))


def answer_queries(nums, queries, limit): 
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    # print(prefix)
    ans = []

    for query in queries:
        if query[0] == 0:
            subarray_sum = prefix[query[1]]
        else:
            subarray_sum = prefix[query[1]] - prefix[query[0] - 1]
        if subarray_sum < limit:
            ans.append(True)
        else:
            ans.append(False)

    return ans


# nums = [1, 6, 3, 2, 7, 2]
# queries = [[0, 3], [2, 5], [2, 4]]
# limit = 13
# print(answer_queries(nums, queries, limit))


def split_array(nums) -> int: 
    """
    num of ways to split array so that sum left half > sum right half 
    """
    n = len(nums) 
    pref = [nums[0]]
    for i in range(1, n):
        pref.append(nums[i] + pref[-1])
    print(pref)

    left = count = 0 

    for right in range(n-1):
        left_sum = pref[right] - pref[left] + nums[left]
        right_sum = pref[-1] - left_sum
        # print(left_sum, right_sum)
        # print('')
        if left_sum >= right_sum:
            count += 1 

    return count

# nums = [10,4,-8,7]
# print(split_array(nums))


def min_start_value(nums): 
    n = len(nums)     
    prefix = [nums[0]]
    ans = max(1, 1 - prefix[0])

    for i in range(1, n):
        prefix.append(nums[i] + prefix[-1])
        start_val = 1 - prefix[-1]
        ans = max(ans, start_val)

    return ans

# nums = [-3,2,-3,4,2]
# nums = [1,-2, -3]
# nums = [-3,6,2,5,8,6]
# print(min_start_value(nums))


def k_radius_avg(nums, k): 
    
    if k == 0:
        return nums
    
    n = len(nums)
    prefix_sums = [nums[0]]
    for x in range(1, n):
        prefix_sums.append(nums[x] + prefix_sums[-1])

    radius_avgs = []

    for i in range(k):
        radius_avgs.append(-1)
    
    for j in range(k, n - k): 
        radius_avgs.append(nums[j] / (2*k) + 1)
        # avg = 

    for m in range(n - k, n):
        radius_avgs.append(-1)

    return radius_avgs


nums = [7,4,3,9,1,8,5,2,6]
k = 3
print(k_radius_avg(nums, k))
