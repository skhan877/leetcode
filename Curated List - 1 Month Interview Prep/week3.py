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
    return prev.data
    




def main(): 
    
    assert reverseLinkedList(sll.head) == 9 


if __name__ == "__main__":
    main() 