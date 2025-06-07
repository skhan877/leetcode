def binary_search(arr: list[int], x: int) -> bool:
    
    l = 0 
    r = len(arr) - 1 

    arr = sorted(arr) 

    while l <= r:
        mid = (l + r) // 2
        if x == arr[mid]: 
            return True 
        elif x < arr[mid]: 
            r = mid - 1
        elif x > arr[mid]:
            l = mid + 1
    
    return False

# a = [2,5,4,3,7,1]
# print(binary_search(a, 71)) 

def binary_search_dupes(arr: list[int], x: int) -> int:
    n = len(arr)
    left = 0 
    right = n

    arr = sorted(arr) 

    while left < right: 
        mid = (left + right) // 2 
        if x > arr[mid]:
            left = mid + 1
        elif x <= arr[mid]:   # CHANGE THIS TO < FOR INSERTION POINT
            right = mid 

    return left


# a = [2,5,4,2,7,3,7,1]
# print(binary_search_dupes(a, 4))


def successful_pairs(spells, potions, success): 
    
    pairs = [0] * len(spells)

    def binary_search(arr, x): 
        arr = sorted(arr)
        l = 0
        r = len(arr) - 1 
        while l <= r:
            m = (l + r) // 2
            if arr[m] < x: 
                l = m + 1 
            else:
                r = m - 1
        return l
    

    for i in range(len(spells)): 
        target = success / spells[i] 
        potions_indx = binary_search(potions, target)
        # print(spells[i], target, potions_indx, len(potions) - potions_indx)
        pairs[i] = len(potions) - potions_indx

    return pairs 

spells = [3,1,2]
potions = [8,5,8]
success = 16

print(successful_pairs(spells, potions, success))