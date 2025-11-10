"""
Top Interview Questions 
Easy

Linked Lists
"""

# class ListNode(): 
#     def __init__(self, x):
#         self.val = x 
#         self.next = None 
    


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

def reverse_list(head):
    prev = None 
    while head: 
        cur = head 
        head = head.next 
        cur.next = prev 
        prev = cur 
    return head 
    
def merge_lists(list1, list2): 
    
    if not list1 and not list2:
            return list1
        
    else:
        merged = []
        while list1: 
            if list2:
                if list1.val <= list2.val:
                    merged.append(list1.val)
                    list1 = list1.next
                elif list2.val < list1.val: 
                    merged.append(list2.val)
                    list2 = list2.next
            else:
                merged.append(list1.val)
                list1 = list1.next

        while list2:
            merged.append(list2.val)
            list2 = list2.next 

        head = ListNode(merged[0])
        current = head 

        for item in merged[1:]:
            current.next = ListNode(item)
            current = current.next 

        return head 

def palindome(head): 
    if not head: return True 
    arr = [] 
    while head: 
        arr.append(head.val)
        head = head.next 
    
    return arr[::] == arr[::-1]




#######################################################################
####################### starting again 26.10.25 #######################
#######################################################################


class ListNode(): 
    def __init__(self, val):
        self.val = val 
        self.next = None 


def delete_node(node): 
    node.val = node.next.val 
    node.next = node.next.next 

"""
def remove_nth_last_node(head, n): 
    len_list = 0 
    temp = head 
    while temp: 
        len_list += 1 
        temp = temp.next 
    # print(len_list)
 
    remove_idx = len_list - n
    curr = head
    i = 0 
    while i < remove_idx:
        curr = curr.next
        i += 1
    
    curr.val = curr.next.val 
    curr.next = curr.next.next 

    return head 
"""  

def reverse_list(head): 
    pass 



def main():

    # assert palindome(head) == False 

    print(reverse_list(head))

    # assert(remove_nth_last_node(head, 4)) == [5,1,9]
    # assert(remove_nth_last_node(head, 2)) == [4,5,9]
    # assert(remove_nth_last_node(head, 1)) == [4,5,1]



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