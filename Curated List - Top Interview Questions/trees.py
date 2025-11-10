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
    pass 

def target_sum(node): 
    pass 


def main(): 
    # preorder(root)
    # inorder(root)
    postorder(root)


if __name__ == "__main__":
    main() 
