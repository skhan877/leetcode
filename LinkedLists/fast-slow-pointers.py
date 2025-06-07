class ListNode:
    def __init__(self, val): 
        self.val = val 
        self.next = None 

one = ListNode(1) 
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

head = one
one.next = two 
two.next = three 
three.next = four 
four.next = five 

print(f'{head.val} -> {head.next.val} -> {head.next.next.val} -> {head.next.next.next.val} -> {head.next.next.next.next.val}')
print('')


def middle_node(head): 
    if not head: 
        return

    # find length of list 
    length = 0 
    dummy = head
    while dummy: 
        length += 1
        dummy = dummy.next

    # calc middle index 
    mid = length // 2

    # find mid node 
    for i in range(mid):
        head = head.next

    return head.val

# print(middle_node(head))

def middle_node_better(head): 
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
    return slow.val

# print(middle_node_better(head))

six = ListNode(6)
five.next = six

def has_cycle(head): 
    # cycle can be anywhere within the list, not necessarily from tail to head! 
    slow = head 
    fast = head 
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next 
        if fast == slow:
            return True
    return False 
    
# print(has_cycle(head))


def find_node(head, k):
    slow = head 
    fast = head 

    for i in range(k):
        fast = fast.next 
    
    while fast: 
        slow = slow.next 
        fast = fast.next 
    
    return slow.val 

# print(find_node(head, 2))

def middle_node(head): 
    slow = head 
    fast = head 

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
    
    return slow.val 

# print(middle_node(head))

def delete_dupes(head): 
    cur = head

    while cur.next: 
        if cur.val ==  cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return head

print(delete_dupes(head))