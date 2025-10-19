"""
Top Interview Questions 
Easy

Arrays
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
    print(nums)
    return nums 

def single_num(arr):
    if len(arr) == 1:
        return arr[0] 
    arr = sorted(arr) 
    p, q = 0, 1
    while q < len(arr): 
        if arr[p] == arr[q]:
        # if arr[p] ^ arr[q] == 0:
            p += 2 
            q += 2 
        else:
            break  
    return arr[p]

def intersect(nums1, nums2): 
    result = []
    for num in nums1: 
        if num in nums2:
            result.append(num)
            nums2.remove(num)
            if not nums2:
                break
    return result

def plus_one(digits): 
    s = "".join(map(str, digits))
    s = [int(x) for x in str(int(s) + 1)]
    return s 

def move_zeroes(nums): 
    n = len(nums)
    for i in range(n-1, -1 , -1): 
        if nums[i] == 0: 
            nums.append(nums.pop(i))
    return nums 

def two_sum(nums, target): 
    
    for i in range(len(nums)-1): 
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j] 

def valid_sudoku(M): 
    from collections import Counter 

    n = len(M)
    
    def valid_array(arr): 
        counts = Counter(arr)
        result = True 
        for k, v in counts.items(): 
            if k != "." and v > 1:
                result = False
        return result  
            

    checks = []

    # check rows 
    for i in range(n): 
        checks.append(valid_array(M[i]))

        # check cols
        col = [] 
        for j in range(n): 
            col.append(M[j][i])
        checks.append(valid_array(col))

    # 3x3 grids
    subgrids = []
    x = 3
    while x <= n:
        grid = [M[i][j] for i in range(0,3) for j in range(x-3, x)]
        x += 3
        subgrids.append(grid)

    x = 3
    while x <= n:
        grid = [M[i][j] for i in range(3,6) for j in range(x-3, x)]
        x += 3
        subgrids.append(grid)

    x = 3
    while x <= n:
        grid = [M[i][j] for i in range(6,9) for j in range(x-3, x)]
        x += 3
        subgrids.append(grid)

    for sub in subgrids:
        checks.append(valid_array(sub)) 

    return False not in checks

def rotate(matrix): 
    pass 




#######################################################################
####################### starting again 19.10.25 #######################
#######################################################################

def remove_duplicates(nums): 
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            del nums[i]
        else:
            i += 1

    # print(nums)
    return len(nums)

def max_profit(prices): 
    daily_pnl = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    max_pnl = sum([pnl for pnl in daily_pnl if pnl > 0])
    return max_pnl

def single_num(nums): 
    result = 0 
    for i in range(len(nums)):
        result ^= nums[i] 
    return result 


def main(): 

    # assert rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]] 

    # board1 = [["5","3",".",".","7",".",".",".","."]
    #         ,["6",".",".","1","9","5",".",".","."]
    #         ,[".","9","8",".",".",".",".","6","."]
    #         ,["8",".",".",".","6",".",".",".","3"]
    #         ,["4",".",".","8",".","3",".",".","1"]
    #         ,["7",".",".",".","2",".",".",".","6"]
    #         ,[".","6",".",".",".",".","2","8","."]
    #         ,[".",".",".","4","1","9",".",".","5"]
    #         ,[".",".",".",".","8",".",".","7","9"]]
    
    # board2 = [["8","3",".",".","7",".",".",".","."]
    #         ,["6",".",".","1","9","5",".",".","."]
    #         ,[".","9","8",".",".",".",".","6","."]
    #         ,["8",".",".",".","6",".",".",".","3"]
    #         ,["4",".",".","8",".","3",".",".","1"]
    #         ,["7",".",".",".","2",".",".",".","6"]
    #         ,[".","6",".",".",".",".","2","8","."]
    #         ,[".",".",".","4","1","9",".",".","5"]
    #         ,[".",".",".",".","8",".",".","7","9"]]
    
    # assert valid_sudoku(board1) == True 
    # assert valid_sudoku(board2) == False

    # assert two_sum([2,7,11,15], 9) == [0,1]
    # assert two_sum([3,2,4], 6) == [1,2]
    # assert two_sum([3,3], 6) == [0,1]
    
    # assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0]
    # assert move_zeroes([0]) == [0]
    
    # assert plus_one([1,2,3]) == [1,2,4]
    # assert plus_one([4,3,2,1]) == [4,3,2,2]
    # assert plus_one([9]) == [1,0]
    # assert plus_one([0]) == [1]
    
    # assert intersect([1], [2,2,1]) == [1]
    # assert intersect([1], [2,2]) == []
    # assert intersect([1,2,2,1], [2,2]) == [2,2]
    # assert intersect([4,9,5], [9,4,9,8,4]) == [4,9]
    
    assert single_num([1,2,1]) == 2 
    assert single_num([2,2,1]) == 1
    assert single_num([4,1,2,1,2]) == 4
    assert single_num([1]) == 1
    
    # assert rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]
    # assert rotate([-1,-100,3,99], 2) == [3,99,-1,-100]
    
    assert max_profit([7,1,5,3,6,4]) == 7
    assert max_profit([1,2,3,4,5]) == 4
    assert max_profit([7,6,4,3,1]) == 0
    
    assert remove_duplicates([1,1,2]) == 2
    assert remove_duplicates([0,0,1,1,1,2,2,3,3,4]) == 5



if __name__ == "__main__": 
    main() 