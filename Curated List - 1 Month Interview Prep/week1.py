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


def main(): 

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