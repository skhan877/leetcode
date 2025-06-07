#####################################
###### SINGLY LINKED LIST ###########
#####################################

class ListNode:
    def __init__(self, val): 
        self.val = val 
        self.next = None 

one = ListNode(1) 
two = ListNode(2)
three = ListNode(3)

head = one
one.next = two 
two.next = three 

print(f'{head.val} -> {head.next.val} -> {head.next.next.val}')
print('')


def add_node(prev_node, node_to_add): 
    node_to_add.next = prev_node.next 
    prev_node.next = node_to_add


def delete_node(prev_node):
    prev_node.next = prev_node.next.next




def get_sum(head): 
    ans = 0 
    while head:
        ans += head.val 
        head = head.next
    return ans 

# print(get_sum(head))


def get_sum_recursive(head):
    if not head:
        return 0 
    
    return head.val + get_sum(head.next)

# print(get_sum_recursive(head))

"""
Use dummy pointers to ensure head reference unchanged
"""
def get_sum_dummy(head): 
    ans = 0 
    dummy = head 

    while dummy:
        ans += dummy.val 
        dummy = dummy.next 
    
    return dummy 





#####################################
###### DOUBLY LINKED LIST ###########
#####################################

class DLLNode:
    def __init__(self, val):
        self.val = val 
        self.next = None 
        self.prev = None 

def add_node_dll(node, node_to_add):
    prev_node = node.prev 
    prev_node.next = node_to_add
    node_to_add.next = node    
    node_to_add.prev = prev_node 
    node.prev = node_to_add

def delete_node_dll(node): 
    prev_node = node.prev 
    next_node = node.next 
    prev_node.next = next_node 
    next_node.prev = prev_node 

### using "sentinal" nodes for head and tail, rather than actual node
### makes it O(1) when using specific reference point to easily add or remove
### nodes from the start or end of the linked list. 

head = DLLNode(None)
tail = DLLNode(None)
head.next = tail 
tail.prev = head 


def add_to_end_dll(node_to_add): 
    node_to_add.next = tail 
    node_to_add.prev = tail.prev
    tail.prev.next = node_to_add
    tail.prev = node_to_add

def del_from_end_dll():
    if head.next == tail:
        return 

    node_to_remove = tail.prev 
    node_to_remove.prev.next = tail 
    tail.prev = node_to_remove.prev 

def add_to_start_dll(node_to_add):
    node_to_add.prev = head 
    node_to_add.next = head.next
    head.next.prev = node_to_add
    head.next = node_to_add 

def remove_from_start(): 
    if head.next == tail: 
        return 

    node_to_remove = head.next 
    node_to_remove.next.prev = head
    head.next = node_to_remove.next


one = DLLNode(1)
two = DLLNode(2)
three = DLLNode(3)
add_to_start_dll(one)
add_to_end_dll(two)
add_to_end_dll(three)

print(f'{head.next.val} <-> {head.next.next.val} <-> {head.next.next.next.val}')
print('')

