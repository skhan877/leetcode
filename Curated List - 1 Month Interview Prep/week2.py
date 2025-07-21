from collections import Counter 


def sockMerchant(n, ar): 
    freq = Counter(ar) 
    pairs = 0 
    for v in freq.values(): 
        pairs += v // 2 
    return pairs 

def findZigZagSequence(a, n): 
    a.sort()
    mid = int(n/2)
    a[mid], a[n-1] = a[n-1], a[mid] 

    st = mid + 1
    ed = n - 2  
    while(st < ed): 
        a[st], a[ed] = a[ed], a[st] 
        st = st + 1
        ed = ed - 1 

    return a

def pageCount(n, p):     
    pages_from_start = (p // 2)
    pages_from_end = (n - p) // 2 
    if n % 2 == 0: 
        pages_from_end = (1 + n - p) // 2 

    return min(pages_from_end, pages_from_start)


def main(): 

    assert pageCount(6, 2) == 1 
    assert pageCount(5, 3) == 1 
    assert pageCount(15, 15) == 0 
    assert pageCount(7, 5) == 1

    assert findZigZagSequence([2,3,5,1,4,9,7,6,8], 9) == [1,2,3,4,9,8,7,6,5]
    assert findZigZagSequence([2,3,5,1,4], 5) == [1,2,5,4,3]
    
    assert sockMerchant(7, [1,2,1,2,1,3,2]) == 2
    assert sockMerchant(9, [10, 20, 10, 20, 10, 30, 50, 10, 20]) == 3


if __name__ == "__main__":
    main() 
