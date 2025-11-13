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

def valid_parens(s: str) -> bool: 
    if len(s) == 0: return True 
    if len(s) == 1: return False 
    closing_to_open_map = {
        ")" : "(",
        "]" : "[", 
        "}" : "{",
    }
    stack = [] 
    for p in s: 
        if p in closing_to_open_map.values():
            stack.append(p)
        else:
            # is a closing parenth
            if closing_to_open_map[p] == stack[-1]:
                stack.pop()
            else:
                return False  
    return True 

def max_profit(prices): 
    max_prof = 0 
    n = len(prices) 
    p, q = 0, 1 
    while q < n: 
        cur_prof = prices[q] - prices[p]
        max_prof = max(max_prof, cur_prof) 
        if cur_prof < 0: 
            p = q 
        q += 1 
    return max_prof



def main(): 
    # assert basic_calculator_two(s="30+2*2") == 34

    assert min_operations("001") == 1 

    assert valid_parens("()") == True 
    assert valid_parens("{[]}") == True
    assert valid_parens("{]}") == False 

    assert max_profit([7,1,5,3,6,4]) == 5 
    assert max_profit([7,6,4,3,1]) == 0 

if __name__ == "__main__": 
    main() 