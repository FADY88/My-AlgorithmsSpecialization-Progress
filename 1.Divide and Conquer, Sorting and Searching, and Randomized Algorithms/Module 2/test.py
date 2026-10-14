x = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n = len(x)
mid = n // 2
a = [x[0][0:mid], x[1][0:mid]]

b = [x[0][mid:n], x[1][mid:n]]

c = [x[mid][0:mid], x[mid + 1][0:mid]]

d = [x[mid][mid:n], x[mid + 1][mid:n]]
d[1][1] = 999999
print(x)
print(a)
print(b)
print(c)
print(d)
for i in range(3):
  print(i)

def MatrixAdd(x, y):
  main = []
  for i in range(len(x)):
    sub = []
    for j in range(len(x)):
      sub.append(x[i][j] + y[i][j])
    main.append(sub)
  return main

print(MatrixAdd(a, b))


ans = []
for i in range(mid):
  ans.append(a[i] + b[i])
for i in range(mid):
  ans.append(c[i] + d[i])

print(x)
print(ans)