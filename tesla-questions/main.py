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

def balloons(text: str) -> int: 
    from collections import Counter
    ch_count = Counter(text) 
    max_inst = min(ch_count["b"], ch_count["a"], ch_count["n"], ch_count["l"] // 2, ch_count["o"] // 2)
    return max_inst

def move_zeroes(nums):
    n = len(nums) 
    for i in range(n-1, -1, -1):
        if nums[i] == 0:
            nums.append(nums.pop(i))
    return nums

def decode_message(key: str, message: str) -> str: 
    unique_key = []
    for k in key:
        if k not in unique_key and k.isalpha():
            unique_key.append(k)
    alphabet = [ch for ch in "abcdefghijklmnopqrstuvwxyz"]
    key_map = {unique_key[i]: alphabet[i] for i in range(len(unique_key))}
    key_map[" "] = " "
    decoded = "".join([key_map[x] for x in message])
    return decoded 

def is_anagram(s: str, t: str) -> bool: 
    from collections import Counter 
    return Counter(s) == Counter(t)

class MovingAverage:
    def __init__(self, size: int): 
        self.size = size 
        self.vals = []
        self.avgs = [] 
    
    def next(self, val: int) -> float: 
        self.val = val 
        self.vals.append(self.val)
        if len(self.vals) < self.size: 
            n = len(self.vals)
        else:
            n = self.size 
        self.avgs.append(sum(self.vals[-n:]) / n) 
        return self.avgs

    def view_history(self):
        print(self.vals)



def main(): 

    mv = MovingAverage(3); mv.next(1); mv.next(10); mv.next(3)
    assert mv.next(5) == [1.0, 5.5, 4.666666666666667, 6.0]

    # assert basic_calculator_two(s="30+2*2") == 34

    assert min_operations("001") == 1 

    assert valid_parens("()") == True 
    assert valid_parens("{[]}") == True
    assert valid_parens("{]}") == False 

    assert max_profit([7,1,5,3,6,4]) == 5 
    assert max_profit([7,6,4,3,1]) == 0 

    assert balloons("nlaebolko") == 1 
    assert balloons("loonbalxballpoon") == 2 
    assert balloons("leetcode") == 0
    assert balloons("ballon") == 0
    assert balloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw") == 10

    assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0]
    assert move_zeroes([0]) == [0]
    assert move_zeroes([0,0,1]) == [1,0,0]

    assert decode_message(key="the quick brown fox jumps over the lazy dog", message="vkbs bs t suepuv") == "this is a secret"
    assert decode_message(key="eljuxhpwnyrdgtqkviszcfmabo", message="zwx hnfx lqantp mnoeius ycgk vcnjrdb") == "the five boxing wizards jump quickly"

    assert is_anagram("anagram", "nagaram") == True 
    assert is_anagram("rat", "car") == False


if __name__ == "__main__": 
    main() 