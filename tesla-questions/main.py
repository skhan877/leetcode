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

def tictactoe(moves) -> str: 
    grid = [["", "", ""], ["", "", ""] ,["", "", ""]] 
    num_moves = 0 
    
    for i in range(len(moves)): 
        row, col = moves[i][0], moves[i][1]
        
        if i % 2 == 0:      # player 1 
            grid[row][col] = "X"
            num_moves += 1
        else:               # player 2
            grid[row][col] = "O"

        if num_moves >= 3: 
            # start checking for winner 
            # check row: 
            for row in grid:
                horizontal =  row[0] + row[1] + row[2] 
                if horizontal ==  "XXX": return "A"
                elif horizontal == "OOO": return "B"
            # check cols:
            for i in range(len(grid)):
                vertical = grid[0][i] + grid[1][i] + grid[2][i] 
                if vertical == "XXX": return "A"
                elif vertical == "OOO": return "B"
            # check diag:
            diag1 = grid[0][0] + grid[1][1] + grid[2][2]
            diag2 = grid[2][0] + grid[1][1] + grid[0][2]
            if diag1 == "XXX" or diag2 == "XXX": return "A"
            elif diag1 == "OOO" or diag2 == "OOO": return "B"
            
            else:
                return "Pending"

    filled = 0 
    for row in grid:
        if "" not in row:
            filled += 1 

    return "Draw" if filled == 3 else -1

def longest_substring(s: str) -> int: 
    from collections import defaultdict

    if len(s) < 1:
        return len(s)

    d = defaultdict(int) 
    l = ans = 0
    d[s[l]] == 1 

    for r in range(len(s)):
        d[s[r]] += 1
        while d[s[r]] > 1:
            d[s[l]] -= 1
            l += 1
        ans = max(ans, r - l + 1)
    
    return ans

def longest_palindome(s: str) -> int: 
    n = len(s) 
    if n <= 1:
        return n 

    else:

        res = ""    
        maxLen = 0 

        if n % 2 == 0:  
            for i in range(n):
                p, q = i, i + 1
                while p >= 0 and q < n and s[p] == s[q]:
                    curLen = q - p + 1
                    if curLen > maxLen:
                        maxLen = curLen 
                        print(s[p: q + 1])
                        res = s[p:q+1]
                    p -= 1
                    q += 1
    
        elif n % 2 != 0:
            for i in range(n):
                p, q = i, i 
                while p >= 0 and q < n and s[p] == s[q]:
                    curLen = q - p + 1
                    if curLen > maxLen:
                        maxLen = curLen 
                        print(s[p: q + 1])
                        res = s[p:q+1]
                    p -= 1
                    q += 1
    
        print("hello", res, maxLen)
        return res 



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

    # assert tictactoe([[0,0], [2,0], [1,1], [2,1], [2,2]]) == "A"
    # assert tictactoe([[0,0], [2,0], [1,1], [2,1], [0,2]]) == "Pending"
    # assert tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]) == "B"

    assert longest_substring("abcabcab") == 3
    assert longest_substring("bbbbbb") == 1
    assert longest_substring("") == 0 
    assert longest_substring("s") == 1 
    assert longest_substring("pwwkew") == 3 
    assert longest_substring("au") == 2

    print(longest_substring("cbbd"))
    # assert longest_substring("cbbd") == "bb"
    # assert longest_palindome("babad") == "bab"
    

if __name__ == "__main__": 
    main()
