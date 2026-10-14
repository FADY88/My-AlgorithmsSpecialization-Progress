print("queue")
l = [1, 2, 3, 4, 5]
print(l)
l.append(6)
print(l)
l.pop(0)
print(l)

print("stack")
l = [1, 2, 3, 4, 5]
print(l)
l.append(6)
print(l)
l.pop()
print(l)

while len(l):
  print(len(l))
  l.pop()

d = {1: 3, 4: 3}
for i in d:
  print(i)
  
def test():
  print(l)

test()
import sys
print(sys.getrecursionlimit())
n = 5
def test(g):
  print(n)
  print(len(g))
G = {1: [2, 3], 2: [3], 3: [4], 4: []}
print(len(G))
test(G)