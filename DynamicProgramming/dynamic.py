def fib_normal(n): 
    if n <= 1:
        return n 
    
    return fib_normal(n-1) + fib_normal(n-2)

# print(fib_normal(5))

def fib_dynamic(n):
    if n <= 1:
        return n 

    if n in memo: 
        return memo[n]
    
    memo[n] = fib_dynamic(n-1) + fib_dynamic(n-2)
    return memo[n]

# memo = {}
# for i in range(10):
#     print(i, fib_dynamic(i)) 


def min_cost_stair_climb(cost) -> int:
    def dp(i): 
        if i <= 0: return 0 
        if i in memo: return memo[i]

        memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
        return memo[i] 
    
    memo = {}
    return dp(len(cost))


def house_robber(nums): 
    def dp(i): 
        if i == 0: nums[0]
        if i == 1: max(nums[0], nums[1])
        if i in memo: return memo[i]
        memo[i] = max(nums[i] + dp(i-2), dp(i-1)) 
        return memo[i] 
    
    memo = {}
    houses = len(nums) 
    return dp(houses - 1)


from functools import cache 

# @cache
memo = {} 
def fibo(n): 
    if n <= 1: return n 
    if n in memo: return memo[n]
    memo[n] = fibo(n-1) + fibo(n-2)
    print(memo)
    return memo[n]

print(fibo(5))