def pangram(s: str) -> bool:
    """
    check every letter is used
    """
    n = len(s)
    d = dict() 
    l = []
    for i in range(n):
    #     if s[i] not in d:
    #         d[s[i]] = 1
    #     else:
    #         d[s[i]] += 1 
    
    # return len(d) == 26

        curr = chr(ord('a') + i)
        l.append(curr)

    return l 

# s = "thequickbrownfoxjumpsovethelazydog"
s = 'leetcode'
# print(pangram(s))


def missing_number(nums) -> int: 
    """
    return the num that is missing 
    """
    nums_set = set(nums)
    n = len(nums) 
    for i in range(n+1):  # O(n)
        if i not in nums_set:  # O(1) constant time when checking a set (would be O(n) if checking in list)
            return i 
    

n = [0,1,3]
# print(missing_number(n))

# from collections import defaultdict 

def counting(s: str, k: int) -> int: 
    """
    length of longest substring with at most k distinct chars 
    """
    n = len(s)
    d = dict()
    left = ans = 0 

    def add_to_dict(dic, x):
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
        return dic

    for right in range(n): 
        add_to_dict(d, s[right])
        while len(d) > k:
            d[s[left]] -= 1 
            if d[s[left]] == 0:
                del d[s[left]]
            left += 1
        ans = max(ans, right - left + 1)
        
    return ans


s = 'eceecba'
# print(counting(s, 2))

def longest_substring(s: str, k: int) -> int: 
    n = len(s) 
    d = dict() 
    left = ans = 0 

    for right in range(n): 
        if s[right] not in d:
            d[s[right]] = 1
        else:
            d[s[right]] += 1
        while len(d) > k: 
            d[s[left]] -= 1 
            if d[s[left]] == 0:
                del d[s[left]]
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans

# print(longest_substring(s, 2))


def intersection(nums): 
    """
    2248. Return sorted array of nums that appear in each array.
    """
    def add_to_dict(d, x): 
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

    n = len(nums)
    d = dict()

    for lst in nums:
        for el in lst:
            add_to_dict(d, el)
    
    result = sorted([num for num in d if d[num]==n])

    return result 


# nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# print(intersection(nums))
    

def equal_occurrances(s: str) -> bool:
    n = len(s) 
    d = dict() 

    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
        
    vals = set(d.values())
    return len(vals) == 1

# s = "aaabb"
# print(equal_occurrances(s))

from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int: 
    """
    560: num of subs whose sum == k 
    """
    counts = defaultdict(int)
    counts[0] = 1 
    ans = curr = 0

    for num in nums: 
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1 
    
    return ans 


# nums = [1, 2, 1, 2, 1]
# k = 3
# nums = [1, -1, 1, -1]
# k = 0
# print(subarray_sum(nums, k))


def nice_subarrays(nums, k): 
    """
    1248: num of subs with k odd numbers in it
    """
    counts = defaultdict(int) 
    curr = ans = 0 
    counts[0] = 1

    for num in nums:
        pass 

        
nums = [1, 1, 2, 1, 1]
k = 3 

# print(nice_subarrays(nums, k))

from collections import defaultdict
def find_winners(matches): 
    winners = defaultdict(int)
    losers = defaultdict(int)

    for match in matches: 
        winners[match[0]] += 1 
        losers[match[1]] += 1 

    ans = [[], []] 

    for k, v in losers.items():
        if v == 1:
            ans[1].append(k) 
    
    for winner in winners: 
        if winner not in losers:
            ans[0].append(winner)

    ans[0] = sorted(ans[0]) 
    ans[1] = sorted(ans[1])

    return ans

# matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# print(find_winners(matches))


def largest_unique(nums) -> int:
    n = len(nums) 
    d = defaultdict(int)
    ans = -1 

    for _ in nums: 
        d[_] += 1 
    
    for k, v in d.items():
        if v == 1:
            ans = max(ans, k)

    return ans 

# nums = [5,7,3,9,4,9,8,3,1]
# print(largest_unique(nums))


def balloon(text) -> int: 
    target = defaultdict(int)
    for char in "balloon": 
        target[char] += 1 

    available = defaultdict(int) 
    for char in text: 
            available[char] += 1 

    ans = min([available[c] // target[c] for c in target])

    return ans 


# text = "bbbaalloon"
# print(balloon(text))

def group_anagrams(strs): 
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)

    return groups.values()

# strs = ["eat","tea","tan","ate","nat","bat"]
# print(group_anagrams(strs))


def min_card_pickup(cards: list[int]) -> int:
    d = defaultdict(list)
    for i in range(len(cards)): 
        d[cards[i]].append(i)

    sub_lengths = [v[-1] - v[0] for v in d.values() if len(v) > 4]
    if sub_lengths:
        ans = min(sub_lengths)
        return ans 
    else:
        return -1 
    

# cards = [1, 2, 6, 2, 1]
# print(min_card_pickup(cards))


def max_pair_sum(nums: list[int]) -> int: 
    sums_dict = defaultdict(list)

    def calc_digitsum(n: int) -> int: 
        s = 0 
        while n: 
            s += n % 10 
            n //= 10 
        return s

    for i in range(len(nums)): 
        digitsum = calc_digitsum(nums[i])
        # print(i, nums[i], digitsum)
        sums_dict[digitsum].append(i)

    ans = 0 

    for k, v in sums_dict.items(): 
        if len(v) == 2: 
            ans = max(ans, nums[v[0]] + nums[v][1]) 

    return ans if ans != 0 else -1
    

def equal_pairs(grid: list[list[int]]) -> int:
    d = defaultdict(list)
    pass


# grid = [[3,2,1],[1,7,6],[2,7,7]]
# print(equal_pairs(grid))

def ransom_note(note: str, magazine: str) -> bool: 
    note_dict = defaultdict(int)
    mag_dict = defaultdict(int)

    for c in note: 
        note_dict[c] += 1 
    
    for c in magazine: 
        mag_dict[c] += 1 
    
    return False not in [note_dict[k] <= mag_dict[k] for k in note_dict.keys()]


# n = 'aa'
# m = 'ab'
# print(ransom_note(n, m))

def jewels_in_stones(jewels: str, stones: str) -> int: 
    from collections import Counter 

    j = Counter(jewels)
    s = Counter(stones)

    return sum([s[k] for k in j.keys()])

# jewels = "z"
# stones = "aAAbbbb"
# print(jewels_in_stones(jewels, stones))


def substring_non_repeated(s: str) -> int: 

    d = defaultdict(int)
    l = ans = 0
    d[s[l]] == 1

    for r in range(len(s)): 
        d[s[r]] += 1
        print(l, r, d, ans)
        while d[s[r]] > 1:
            d[s[l]] -= 1
            l += 1
        ans = max(ans, r - l + 1)
        
        r += 1

    return ans

# s = "pwwkew"
# print(substring_non_repeated(s))

def contains_dupe(nums: list[int]) -> bool:
    from collections import Counter
    c = defaultdict(int)
    for num in nums: 
        c[num] += 1 
        if c[num] >= 2:
            return True 

    return False 

# nums = [1,1,1,3,3,4,3,2,4,2]
# print(contains_dupe(nums))
# assert contains_dupe(nums) == True


def phone_num(s: str) -> str: 
    num_dict = {"2": "abc", 
               "3": "def",
               "4": "ghi",
               "5": "jkl", 
               "6": "mno",
               "7": "pqrs",
               "8": "tuv", 
               "9": "wxyz",
               " ": " "}
    
    # s_copy = s + " "
    s = s + " "
    converted = []
    counter = 0
    l = 0 
    r = 1 

    for i in range(1, len(s)): 
        counter += 1
        # print(s[i-1], s[i], counter, s[i-counter], converted)
        if s[i] != s[i-1]:
            converted.append(s[i-counter: i])
            counter = 0

    # print("".join(converted))
    # print(converted)

    def convert_nums(num):
        if len(num) > 3 and num[0] not in ["7","9"]:
            # print(num_dict[num[0]])
            return -1
        else:
            return num_dict[num[0]][len(num)-1]

    ans = [convert_nums(n) for n in converted if n != " "]

    return "incorrect string" if -1 in ans else "".join(ans)


num = "2 229997777 7777"
print(phone_num(num))

# assert phone_num(num) == "hey"
assert phone_num(num) == "abyss"