from collections import deque

children = input().split()
toss = int(input())
q = deque(children)
counter = 0
while len(q) > 1:
    counter += 1
    if counter == toss:
       kid = q.popleft()
       print(f"Removed {kid}")
       counter = 0
    else:
        q.append(q.popleft())
print(f"Last is {q[0]}")