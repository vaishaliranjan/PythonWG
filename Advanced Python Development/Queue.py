# Queue is when you add data from one end and can remove data from another end
# Deque or doubled queue is when you can add or remove data from either side

from collections import deque

#its thread safe
friends = deque(('Rolf','Charlie','Jen'))
friends.append("Ritika")
friends.appendleft("Anthony")
print(friends)
friends.pop()
friends.popleft()
print(friends)