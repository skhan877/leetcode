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

def towerBreakers(n, m): 
    if n % 2 == 0 or m == 1: 
        return 2
    else:
        return 1

def caeserCipher(s, k): 
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    rotated = [alphabet[(i + k) % 26] for i in range(26)]
    encrypted = "" 
    for char in s: 
        if char.isalpha():
            position = alphabet.index(char.lower())
            encrypted_char = rotated[position]
            if char.isupper(): 
                encrypted += encrypted_char.upper()
            else:
                encrypted += encrypted_char
        else:
            encrypted += char

    return encrypted 

def dynamicArray(n, queries): 
    arr = [list() for i in range(n)] 
    lastAnswer = 0
    answers = []
    for query in queries:
        op, x, y = query[0], query[1], query[2]
        idx = ((x ^ lastAnswer) % n)
        if op == 1: 
            arr[idx].append(y) 
        else: 
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)

    return answers

def maxMin(arr, k): 
    # FAILING TESTS - WORK NEEDED
    n = len(arr)
    arr = sorted(arr)

    if n == k: 
        diff =  arr[-1] - arr[0]
        return diff

    else:
        minDiff = float("inf") 
        for i in range(n-k):
            subarr = arr[i:i+k] 
            diff = maxMin(subarr, k)
            minDiff = min(minDiff, diff) 
        return minDiff
    
def gridChallenge(grid): 

    def isSorted(arr): 
        n = len(arr) 
        for i in range(1, n): 
            if arr[i-1] > arr[i]: 
                return False 
        return True 

    for r in range(len(grid)):
        if not isSorted(grid[r]):
            grid[r] = sorted(grid[r])

    col_checks = True
    for i in range(len(grid[0])):
        col = ""
        for j in range(len(grid)):
            col += grid[j][i]
        if not isSorted(col):
            col_checks = False
    
    return "YES" if col_checks else "NO"



def main(): 

    assert gridChallenge(['abc','ade','efg']) == "YES"
    assert gridChallenge(['abc','zxy','efg']) == "NO"
    assert gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']) == "YES"
    assert gridChallenge(['abc','lmp','qrt']) == "YES"
    assert gridChallenge(['mpxz','abcd','wlmf']) == "NO"
    assert gridChallenge(['abc','hjk','mpq','rtv']) == "YES"

    assert maxMin([0,0], 2) == 0 
    assert maxMin([1,1], 2) == 0
    assert maxMin([1,10], 2) == 9 
    assert maxMin([1,2,3,4,10,20,30,40,100,200], 4) == 3 
    assert maxMin([1,4,7,2], 2) == 1 
    assert maxMin([1,4,7,2], 3) == 3 

    assert caeserCipher("middle-Outz", 2) == "okffng-Qwvb"

    assert towerBreakers(2, 2) == 2
    assert towerBreakers(2, 6) == 2
    assert towerBreakers(1, 4) == 1

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
