from collections import deque
a=int(input())
b1=deque()
b2=deque()
for i in range(a):
    s=str(input())
    if s.count("+"):
        b2.append(s[2:])
    elif s.count("-"):
        print(b1.popleft())
    else:
        b1.append(s[2:])
    if len(b2)>len(b1):
        b1.append(b2.popleft())
