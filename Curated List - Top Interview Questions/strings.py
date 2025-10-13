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
    
def palindrome(s):
    s = s.lower() 
    s = "".join([ch for ch in s if ch.isalpha() or ch.isnumeric()])
    return s == s[::-1]

def strStr(needle, haystack):
    if needle == haystack:
        return 0 
    p, q = 0, len(needle) 
    while q <= len(haystack): 
        if haystack[p:q] == needle:
            return p 
        else:
            p += 1
            q += 1 
    return -1 

def longest_prefix(strs): 
    shortest = min([len(s) for s in strs]) 
    prefix = [] 
    i = 0
    while i < shortest:
        cur_check = []
        for s in strs:
            cur_check.append(s[i])
        if len(set(cur_check)) == 1:
            prefix.append(cur_check[0])
            i += 1 
        else:
            break 
        
    return "".join(prefix)

def make_anagram(a, b):
    from collections import Counter 
    freq_a, freq_b = Counter(a), Counter(b) 
    in_both = freq_a & freq_b
    tot_chars = len(a) + len(b)

    if not in_both: 
        return tot_chars 
    else: 
        for v in in_both.values(): 
            tot_chars -= (v * 2)
        return tot_chars




#######################################################################
####################### starting again 09.10.25 #######################
#######################################################################


def reverse_string(s): 
    i, j = 0, len(s) -1 
    while i < j: 
        s[i], s[j] = s[j], s[i] 
        i += 1
        j -= 1
    return s 

def reverse_int(n): 
    n = str(n) 
    if n[0] == "-":
        result = "-" + "".join(n[::-1][:-1])
    else:
        result = "".join(n[::-1])

    if not (-2 ** 31 <= int(result) and int(result) <= (2 ** 31) -1):
        return 0 
    else: 
        return int(result)

def first_unique_ch(s): 
    from collections import Counter 
    counts = Counter(s)
    idx = []
    for k, v in counts.items():
        if v == 1:
            idx.append(s.index(k))
    return min(idx) if idx else -1

def anagram(s, t): 
    from collections import Counter 
    return Counter(s) == Counter(t)

def palindrome(s): 
    stripped_s = "".join([ch.lower() for ch in s if ch.isalpha() or ch.isnumeric()])
    i, j = 0, len(stripped_s) - 1 
    while i < j: 
        if stripped_s[i] != stripped_s[j]:
            return False
        i += 1
        j -= 1
    return True 

def strStr(needle: str, haystack: str) -> int: 
    if needle == haystack:
        return 0
    
    p, q = 0, len(needle)
    if q > 1:
        while q <= len(haystack):
            if haystack[p:q] != needle:
                p += 1
                q += 1
            else:
                return p
    return -1


def main(): 

    # assert(make_anagram("cde", "dcf")) == 2
    # assert(make_anagram("cde", "dcf")) == 2
    # assert(make_anagram("", "abc")) == 3
    # assert(make_anagram("abc", "")) == 3
    # assert(make_anagram("abc", "adddd")) == 6
    # assert(make_anagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke")) == 30

    # assert longest_prefix(["car", "cir"]) == "c" 
    # assert longest_prefix(["s", "shop", "shoot"]) == "s" 
    # assert longest_prefix(["flower", "flow", "flight"]) == "fl" 
    # assert longest_prefix(["dog", "racecar", "car"]) == "" 

    assert strStr("s", "s") == 0 
    assert strStr("sad", "sadbutsad") == 0 
    assert strStr("leeto", "leetcode") == -1 

    assert palindrome("A man, a plan, a canal: Panama") == True 
    assert palindrome("race a car") == False 
    assert palindrome(" ") == True 

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