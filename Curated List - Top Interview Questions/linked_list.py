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




def main():
    
    pass
    



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


    main() 