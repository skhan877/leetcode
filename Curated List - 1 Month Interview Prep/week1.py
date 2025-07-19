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


def main(): 
    
    # plusMinus([1,1,0,-1,-1])
    # plusMinus([-4,3,-9,0,4,1])


if __name__ == "__main__":
    main() 