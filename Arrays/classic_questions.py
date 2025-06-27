"""
Top Interview Questions 
Easy
"""

def remove_duplicates(arr): 
    x = 1 
    for i in range(1, len(arr)): 
        if arr[i] != arr[i-1]: 
            arr[x] = arr[i] 
            x += 1 
    return x, arr 


def main(): 
    
    print(remove_duplicates([1,1,2]))



if __name__ == "__main__": 
    main() 