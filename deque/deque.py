import collections
words = ['forest', 'blue', 'cloud', 'sky', 'wood', 'falcon']
deque = collections.deque(words)
print(deque) 
deque.append("site")
print(deque)
deque.appendleft("life")
print(deque)
deque.pop()
print(deque)
deque.popleft()
print(deque)