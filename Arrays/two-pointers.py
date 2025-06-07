def reverseWords(s): 
    
    n = len(s)
    i, j = 0, 0 
    ans = []

    while i < n:
        
        while s[j] != " " and j < n - 1:
        # while j < n:
            # print(s[i], s[j], s[i:j+1])
            j += 1
        
        # print(i, j, s[i], s[j], s[i:j])
        word = s[i:j+1]

        # hacky way of adding a space to the final word (but must copy to new variable so not great)
        if word[-1] != " ":
            word = word + " "
        
        print(word, len(word))
        ans.append(word[::-1])
        print(ans)
        # print('')
        
        i = j + 1
        j = i
        
        # print(i, j)
    
    ans = "".join(ans)
    ans = ans[1:]

    return ans

# s = "Let's take LeetCode contest"
# print(reverseWords(s))


def palindrome(s: str) -> bool:
    if len(s) <= 1: 
        return s 

    l = 0 
    r = len(s) - 1 

    while l < r: 
        if s[l] != s[r]:
            return False 
        l += 1
        r -= 1 

    return True 

# s = "racca"
# print(palindrome(s))


def target_sum_pair(nums, target) -> bool: 
    l = 0 
    r = len(nums) - 1

    while l < r: 
        curr = nums[l] + nums[r]
        if curr == target:
            return True, nums[l], nums[r]
        elif curr > target: 
            r -= 1
        else:
            l += 1 
    
    return False 

# nums = [1, 2, 4, 6, 8, 9, 14, 15] 
# print(target_sum_pair(nums, 10))


def combine_sorted(a, b): 
    ans = [] 
    shorter = min(len(a), len(b))
    i = j = 0

    while i < shorter and j < shorter:
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1 
        elif a[i] > b[j]:
            ans.append(b[j])
            j += 1 
        else: 
            ans.append(a[i])
            ans.append(b[j])
            i += 1
            j += 1
    
    while i < len(a):
        ans.append(a[i])
        i += 1 

    while j < len(b):
        ans.append(b[j])
        j += 1

    return ans


# arr1 = [1, 4, 7, 20]
# arr2 = [3, 5, 6]
# print(combine_sorted(arr1, arr2))


def is_subsequence(s: str, t: str) -> bool:
    """
    pointer at start of each string 
    look for each letter from s in t, while pointer < length of t 
    """
    i = j = 0 

    while i < len(s) and j < len(t): 
        if s[i] == t[j]: 
            i += 1 
        j += 1 

    return i == len(s)

s = "ace"
t = "abcd"
# print(is_subsequence(s, t))            


def reverse_prefix(word, ch) -> str: 
    if ch not in word: 
        return word 
    
    l = r = 0 

    while r < len(word): 
        if word[r] == ch:
            break 
        r += 1

    ans = [word[i] for i in range(l, r+1)]
    remainder = "".join([word[j] for j in range(r+1, len(word))])

    while l < r: 
        ans[l], ans[r] = ans[r], ans[l]
        l += 1
        r -= 1

    ans = "".join(ans) + remainder

    return ans

w = "abcdefg"
c = "d"
print(reverse_prefix(w, c))