"""
Top Interview Questions 
Easy

Linked Lists
"""

class ListNode(): 
    def __init__(self, x):
        self.val = x 
        self.next = None 
    


def delete_note(node): 
    node.val = node.next.val 
    node.next = node.next.next 

def remove_nth_last_node(head, n): 
    list_len = 1
    cur_node = head 
    while cur_node.next:
        list_len += 1 
        cur_node = cur_node.next
    
    node_to_rem = list_len - n 
    i = 0 
    ans = []
    cur_node = head 

    if list_len == 1:
        return ans 
    elif list_len == n:
        cur_node = cur_node.next 
        while cur_node:
            ans.append(cur_node.val)
            cur_node = cur_node.next 
    else: 
        while i < list_len: 
            if i != node_to_rem:
                ans.append(cur_node.val)
            cur_node = cur_node.next 
            i += 1

    return ans 


def main():
        
    assert(remove_nth_last_node(head, 4)) == [5,1,9]
    assert(remove_nth_last_node(head, 2)) == [4,5,9]
    assert(remove_nth_last_node(head, 1)) == [4,5,1]
    



if __name__ == "__main__": 

    node1 = ListNode(4)
    node2 = ListNode(5)
    node3 = ListNode(1)
    node4 = ListNode(9)

    head = node1 
    node1.next = node2 
    node2.next = node3 
    node3.next = node4 

    print(f"{head.val} -> {head.next.val} -> {head.next.next.val} -> {head.next.next.next.val}")
    print("")

    main() 