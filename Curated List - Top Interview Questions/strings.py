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


def main(): 
    
    assert reverse_string(["h","e","l","l","o"]) == ["o","l","l","e","h"]
    assert reverse_string(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]


if __name__ == "__main__":
    main() 