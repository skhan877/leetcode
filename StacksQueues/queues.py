from collections import deque 

queue = deque([1,2,3])
queue.append(4)
queue.append(5) 

queue.popleft() 
queue.popleft() 

print(queue[0]) 
print(len(queue))

