"""
Top Interview Questions 
Easy

Strings
"""

def reverse_string(s): 
    i, j = 0, len(s)-1 
    while i < j: 
        s[i], s[j] = s[j], s[i] 
        i += 1
        j -= 1 
    return s

def reverse_int(x: int) -> int: 
    lst_x = list(str(x))
    if lst_x[0] == "-":
        result = int("-" + "".join(lst_x[::-1][:-1]))
    else:
        result = int("".join(lst_x[::-1]))

    if result >= -2**31 and result <= (2**31)-1: 
        return result 
    else:
        return 0 

def first_unique_ch(s): 
    from collections import Counter 
    counts = Counter(list(s))
    idxs = [] 
    for k, v in counts.items(): 
        if v == 1:
            idxs.append(list(s).index(k))
    return min(idxs) if idxs else -1 

def anagram(s, t): 
    from collections import Counter 
    return Counter(list(s)) == Counter(list(t))
    

def main(): 

    assert anagram("anagram", "nagaram") == True
    assert anagram("rat", "cart") == False

    assert first_unique_ch("leetcode") == 0 
    assert first_unique_ch("aabb") == -1
    assert first_unique_ch("loveleetcode") == 2

    assert reverse_int(-51) == -15
    assert reverse_int(120) == 21 
    
    assert reverse_string(["h","e","l","l","o"]) == ["o","l","l","e","h"]
    assert reverse_string(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]
    






if __name__ == "__main__":
    main() 