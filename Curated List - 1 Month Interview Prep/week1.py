def plusMinus(arr): 
    n = len(arr) 
    pos, neg, zero = 0, 0, 0
    for num in arr: 
        if num == 0:
            zero +=1 
        elif num > 0: 
            pos += 1 
        elif num < 0:
            neg += 1 
    print(format(pos/n, ".6f"))
    print(format(neg/n, ".6f"))
    print(format(zero/n, ".6f"))

def minMaxSum(arr): 
    arr = sorted(arr) 
    minSum = sum(arr[:4])
    maxSum = sum(arr[-4:])
    print(minSum, maxSum)

def pangram(s): 
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    s_set = set(s.lower().replace(" ", ""))
    return "pangram" if alphabet == s_set else "not pangram"

def matchingStrings(strings, queries): 
    result = [strings.count(q) for q in queries]
    return result 

def lonelyInteger(arr): 
    stack = [] 
    for x in sorted(arr): 
        if stack and stack[-1] == x:
            stack.pop(-1)
        else:
            stack.append(x) 
    return stack[-1]

def flippingBits(n): 
    bits = [abs(int(bit) - 1) for bit in bin(n).replace("0b", "")]
    leading_zeros = 32 - len(bits)
    digits = [1] * leading_zeros 
    flipped = "".join([str(d) for d in digits + bits])
    return int(flipped, 2)

def diagDiff(arr): 
    primary = [arr[i][i] for i in range(len(arr))]
    secondary = [arr[i][len(arr)-1-i] for i in range(len(arr))]
    diff = abs(sum(primary) - sum(secondary))
    return diff

def countingSort(arr): 
    freq = [0] * 4
    for idx in arr: 
        freq[idx] += 1 
    # result = []
    # for i in range(len(freq)): 
    #     if freq[i] != 0: 
    #         result.extend([i] * freq[i])
    # return result
    return freq 

def twoArrays(k, A, B): 
    A = sorted(A) 
    B = sorted(B, reverse=True) 
    n = len(A)
    for i in range(n): 
        if A[i] + B[i] < k: 
            return "NO" 
    return "YES"


def main(): 

    assert twoArrays(10, [2,1,3], [7,8,9]) == "YES"
    assert twoArrays(5, [1,2,2,1], [3,3,3,4]) == "NO"
    assert twoArrays(1, [0,1], [0,2]) == "YES"

    assert countingSort([1,1,3,2,1]) == [0,3,1,1]

    assert diagDiff([[1,2,3], [4,5,6], [9,8,9]]) == 2 
    assert diagDiff([[11,2,4], [4,5,6], [10,8,-12]]) == 15 

    assert flippingBits(9) == 4294967286
    assert flippingBits(2147483647) == 2147483648
    assert flippingBits(1) == 4294967294
    assert flippingBits(0) == 4294967295

    assert lonelyInteger([1,2,3,4,3,2,1]) == 4
    assert lonelyInteger([0,0,1,2,1]) == 2

    assert matchingStrings(["ab", "ab", "abc"], ["ab", "abc", "bc"]) == [2, 1, 0]

    assert pangram("hello") == "not pangram"
    assert pangram("The quick brown fox jumps over the lazy dog") == "pangram" 

    # minMaxSum([1,3,5,7,9])
    # minMaxSum([1,2,3,4,5])

    # plusMinus([1,1,0,-1,-1])
    # plusMinus([-4,3,-9,0,4,1])


if __name__ == "__main__":
    main() 