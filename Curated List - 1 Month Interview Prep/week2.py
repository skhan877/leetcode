from collections import Counter 


def sockMerchant(n, ar): 
    freq = Counter(ar) 
    pairs = 0 
    for v in freq.values(): 
        pairs += v // 2 
    return pairs 



def main(): 
    
    assert sockMerchant(7, [1,2,1,2,1,3,2]) == 2
    assert sockMerchant(9, [10, 20, 10, 20, 10, 30, 50, 10, 20]) == 3


if __name__ == "__main__":
    main() 