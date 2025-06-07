def stack_basics():

    stack = [] 

    stack.append(1)
    stack.append(2)
    stack.append(3) 

    stack.pop() #3 
    stack.pop() #2

    # check if empty
    not stack #False

    stack[-1] #1

    len(stack) 

    return stack 


def valid_parantheses(s): 
    close_to_open = {")":"(",
                     "}":"{",
                     "]":"["}
    stack = [] 
    for _ in s:
        if _ in close_to_open:
            if not stack:
                return False 
            elif close_to_open[_] != stack[-1]:
                return False
            else:
                stack.pop()
        else:
            stack.append(_)

    return stack 

# s = "({})"
# s = "(){}[]"
# s = "(]"
# s = "({)}"
# print(valid_parantheses(s))


def remove_dupes(s): 
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
         
        elif ch != stack[-1]:
            stack.append(ch)

        else:
            stack.pop()

    return "".join(stack)

s = "abbaca"
# print(remove_dupes(s))


def backspace_compare(s, t):
    
    def build_stack(strng):
        stack = []
        for char in strng: 
            if char == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)

    return build_stack(s) , build_stack(t)
    

# s = "xywrrmp"
# t = "xywrrm#p"
# print(backspace_compare(s, t))

def simplify_path(path: str) -> str: 
    stack = [] 

    for char in path.split("/"):
        if char != "/":
            stack.append(char)

    for i in range(len(stack)):
        if stack[i] == "..":
            del stack[i-1]

    return stack 

    
    # return "/".join(stack) 


path =  "/home/user/Documents/../Pictures"
print(simplify_path(path))