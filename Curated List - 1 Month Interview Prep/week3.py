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
        
def mergeLists(head1, head2): 
    if not head1: return head2 
    if not head2: return head1 

    merged = SLL() 
    while head1 and head2: 
        if head1.data <= head2.data: 
            merged.insert_node(head1.data)
            head1 = head1.next 
        elif head2.data < head1.data: 
            merged.insert_node(head2.data)
            head2 = head2.next 
    
    while head1:
        merged.insert_node(head1.data)
        head1 = head1.next
    
    while head2: 
        merged.insert_nodeh(head2.data)
        head2 = head2.next 
    
    return merged.head  

def minimumBribes(q): 
    moves = [q[i-1] - i for i in range(1, len(q) + 1)]
    total = 0 
    chaos = False
    print(moves)
    for move in moves:
        if move > 0:
            total += move 
        if move > 2:
            chaos = True 
    if chaos:
        return "Too chaotic"
    else:
        return total 




def main(): 
    
    print(minimumBribes([1,2,5,3,7,8,6,4]))
    assert minimumBribes([4,1,2,3]) == "Too chaotic"
    assert minimumBribes([1,2,3,5,4,6,7,8]) == 1 
    assert minimumBribes([2,1,5,3,4]) == 3
    assert minimumBribes([2,5,1,3,4]) == "Too chaotic"

    assert reverseLinkedList(sll.head).data == 9



if __name__ == "__main__":
    main() 