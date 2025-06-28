"""
Top Interview Questions 
Easy
"""

def remove_duplicates(arr): 
    x = 1 
    for i in range(1, len(arr)): 
        if arr[i] != arr[i-1]: 
            arr[x] = arr[i] 
            x += 1 
    return x, arr 

def max_profit(prices): 
    n = len(prices)
    max_prof = 0 
    for i in range(1, n): 
        if prices[i] >= prices[i-1]: 
            cur_profit = prices[i] - prices[i-1]
            max_prof += cur_profit
    return max_prof

def rotate(nums, k): 
    nums = nums[::-1] 
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    return nums 



def main(): 
    
    assert rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]
    assert rotate([-1,-100,3,99], 2) == [3,99,-1,-100]
    # assert max_profit([7,1,5,3,6,4]) == 7
    # assert max_profit([1,2,3,4,5]) == 4
    # assert max_profit([7,6,4,3,1]) == 0
    # print(remove_duplicates([1,1,2]))



if __name__ == "__main__": 
    main() 