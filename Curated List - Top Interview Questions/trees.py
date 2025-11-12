"""
Top Interview Questions 
Easy

Trees
"""

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.right = right 
        self.left = left  


root = TreeNode(0) 
one = TreeNode(1) 
two = TreeNode(2) 
three = TreeNode(3) 
four = TreeNode(4) 
five = TreeNode(5) 
six = TreeNode(6)

root.left = one 
root.right = two 
one.left = three 
one.right = four 
four.right = six 
two.right = five 

"""
        0
       / \    
      1   2
     / \   \
    3   4   5
         \
          6
"""

def preorder(node): 
    """
    current -> left -> right 
    """
    if not node: 
        return None  

    print(node.val)
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    """
    left -> current -> right
    """
    if not node:
        return 
    
    inorder(node.left)
    print(node.val)
    inorder(node.right)


def postorder(node): 
    """
    left -> right -> current 
    """
    if not node:
        return 
    
    postorder(node.left)
    postorder(node.right)
    print(node.val)


def max_depth(node):
    if not node:
        return 0 
    
    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)

    return max(left_depth, right_depth) + 1


def target_sum(node): 
    pass 

def valid_bst(node):
    """
    5 1 4 null null 3 6 

while node:

    node = 5
    node.left = 1 
    node.right = 4

    node = node.left
        node = 1
        node.left = null 
        node.right = null

        node = node.left 


    lst = 2 1 3 
    n = len(lst)
    root = lst[0] 
    for i in range(1, n):
        if lst[i] 
    
    
    preorder: node, node.left, node.right 
    i = 0 
    n = len(arr) 
    while i < n: 
        childless = [node]
        node = arr[i] 
        node = node.left         
        i += 1 
        
    """


    return 


def main(): 
    # preorder(root)
    # inorder(root)
    # postorder(root)
    print(max_depth(root))
    


if __name__ == "__main__":
    main() 
