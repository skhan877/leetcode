class TreeNode: 
    def __init__(self, val, left=None, right=None): 
        self.val = val 
        self.left = left 
        self.right = right 

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
    current node > left child > right child 
    """
    if not node:
        return 
    
    print(node.val)
    preorder(node.left)
    preorder(node.right)
    return 

# print(preorder(root))

def inorder(node): 
    """
    left child > current node > right child 
    """
    if not node:
        return 
    
    inorder(node.left)
    print(node.val)
    inorder(node.right) 
    return 

# print(inorder(root)) 

def postorder(node):
    """
    left child > right child > current node 
    """

    if not node:
        return 
    
    postorder(node.left)
    postorder(node.right) 
    print(node.val)
    return 

# print(postorder(root))


def max_depth(node): 
    if not node:
        return 0 
    
    left = max_depth(node.left)
    right = max_depth(node.right)

    return max(left, right) + 1
    
# print(max_depth(root))


def target_sum(root, target): 
    def dfs(node, curr):
        if not node:
            return False 
        
        if node.left == None and node.right == None:
            return target == (curr + node.val) 

        curr += node.val 
        left = dfs(node.left, curr)
        right = dfs(node.right, curr)

        return left or right 
    
    return dfs(root, 0)

# print(target_sum(root, 10))


def good_nodes(node):

    if not node.left and not node.right:
        return 1