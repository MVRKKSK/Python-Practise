from collections import deque

deque = deque(["eren" , "mikasa" , "armin" , "reiner"])
deque.append("annie")
deque.append("porcho")
deque.append("bertholt")
print(deque)
deque.popleft()
print(deque)

stack = deque()
