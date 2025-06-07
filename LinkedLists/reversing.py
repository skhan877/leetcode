class ListNode:
    def __init__(self, val): 
        self.val = val 
        self.next = None 

one = ListNode(1) 
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6) 

head = one
one.next = two 
two.next = three 
three.next = four 
four.next = five 
five.next = six 

def print_linked_list(head):
    dummy = head 
    strng = ""
    while dummy:
        strng += " -> " + str(dummy.val)
        dummy = dummy.next

    return strng[4:]

# print(f'{head.val} -> {head.next.val} -> {head.next.next.val} -> {head.next.next.next.val} -> {head.next.next.next.next.val}')
print(print_linked_list(head))
print('')


def reverse_list(head): 
    curr = head 
    prev = None 
    while curr:
        nextnode = curr.next 
        curr.next = prev 
        prev = curr 
        curr = nextnode        
    
    # return prev.val 
    print(print_linked_list(prev))

# print(reverse_list(head))


def swap_nodes(head): 
    h = head 
    prev = None

    # while h:
    #     nextnode = h.next.next 
    #     h.next.next = h
    #     prev = h
    #     h.next = nextnode 

    return


def max_twin_sum(head): 
    # find mid 
    slow = head 
    fast = head 

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
    
    head2 = slow

    # reverse second half of linked list 
    prev = head2
    curr = head2.next
    while curr and curr.next: 
        # print(f'prev: {prev.val}, curr: {curr.val}')
        nextnode = curr.next 
        curr.next = prev 
        prev = curr
        curr = nextnode 
        

    # iterate slow and fast through the halves of the list to find max sum 
    ans = 0 
    dummy = head
    dummy2 = head2

    # while dummy.next:
    #     ans = max(ans, dummy.val + dummy2.val)
    #     dummy = dummy.next 
    #     dummy2 = dummy2.next 
        

    # print(print_linked_list(curr))
    return slow, fast

print(max_twin_sum(head))