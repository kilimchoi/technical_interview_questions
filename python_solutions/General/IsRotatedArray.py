#caltonji 10/31/2015
from collections import deque

A = [1,2,3,5,6,7,8]
B = [5,6,7,8,1,2,3]

C = [1,2,3]
D = [6,7,5,8,1,2,3]

def isRotated(a, b):
    if a == b:
        return True
    if len(a) is not len(b):
        return False
    b = deque(b)
    a = deque(a)
    for i in range(0, len(a)):
        a.append(a.popleft())
        print "a" + str(a) + " b" + str(b) 
        if list(a) == list(b):
            return True
    return False

if __name__ == "__main__":
    print "A and B: " +  str(isRotated(A,B))
    print "B and C: " +  str(isRotated(B,C))
    print "B and D: " +  str(isRotated(B,D))


