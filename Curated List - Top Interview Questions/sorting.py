"""
Top Interview Questions 
Easy

Sorting and Searching
"""

def merge(nums1, nums2, m , n): 
    i = n - 1
    j = n - 1
    k = m - 1
    
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    return nums1

def first_bad(n):
    arr = [i+1 for i in range(n)]
    arr[4] = 1 
    mid = (n + 1) // 2 
    if arr[mid] == 1:
        pass 
    print(mid)


def main(): 

    assert merge([1,2,3,0,0,0], [2,5,6], 6, 3) == [1,2,2,3,5,6]
    
    print(first_bad(5))

if __name__ == "__main__":
    main()