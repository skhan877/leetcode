"""
https://github.com/liquidslr/leetcode-company-wise-problems/tree/main/Tesla
"""

def basic_calculator_two(s: str) -> int: 
    # MEDIUM #
    import re 
    nums = [int(x) for x in re.split("[/*+-]", s)]
    ops = [x for x in s if not x.isnumeric()]
    # print(nums, ops)

    calcs = [[2*2], [], [], []]
    # while ops: 

    result = None 
    return result 

def min_operations(s: str) -> int: 
    if len(s) == 1:
        return 0 
    start0 = 0 
    start1 = 0 
    for i in range(len(s)): 
        if i % 2 == 0: 
            if s[i] == "1": 
                start0 += 1 
            else:
                start1 += 1
        else:
            if s[i] == "1":
                start1 += 1 
            else:
                start0 += 1 
    return min(start0, start1)


def main(): 
    # assert basic_calculator_two(s="30+2*2") == 34
    assert min_operations("001") == 1 

if __name__ == "__main__": 
    main() 


"""
110 

start0: 0 1 0 : odds = 1, evens = 0 
start1: 1 0 1 : odds = 0, evens = 1 

if index == even: 
    if first is 0, all evens should be 0 and all odds should be 1
        otherwise, if odd != 1 or even != 0, start0 += 1
    elif first is 1, all evens should 1 and all odds should be 0 
        otherwise, if odd index != 0 or even index != 1, start1 += 1 

"""