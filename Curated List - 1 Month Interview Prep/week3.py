class Node():
    def __init__(self, data): 
        self.data = data 
        self.next = None

class SLL(): 
    def __init__(self):
        self.head = None 
        self.tail = None 

    def insert_node(self, data): 
        node = Node(data) 
        if not self.head: 
            self.head = node 
        else:
            self.tail.next = node 

        self.tail = node 
    
    def show_list(self):
        node = self.head  
        while node.next: 
            print(node.data, end=" -> ")
            node = node.next
        print(node.data)

sll = SLL() 
sll.insert_node(1)
sll.insert_node(2)
sll.insert_node(5)
sll.insert_node(9)
# sll.show_list() 


def reverseLinkedList(llist): 
    cur = llist 
    prev = None 
    while cur: 
        nxt = cur.next 
        cur.next = prev 
        prev = cur 
        cur = nxt 
    return prev
    
def insertNodeAtPosition(llist, data, position): 
    if not llist:
        llist = SLL() 
        sll.insert_node(data)
    else:
        dummy = llist  
        i = 1
        while i < position: 
            dummy = dummy.next 
            i += 1
        nxt = dummy.next 
        new_node = Node(data) 
        dummy.next = new_node 
        new_node.next = nxt 
    return llist  
        





def main(): 
    
    assert reverseLinkedList(sll.head).data == 9


if __name__ == "__main__":
    main() 