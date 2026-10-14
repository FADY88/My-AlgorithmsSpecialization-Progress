l = [1, 2, 3, 3, 5]
while True:
  i = 0
  while l[i] != 5:
    if l[i] == 4:
      break
    i += 1
  else:
    break
  print("out of inner loop")

print("out of outer loop")

l = (1, 2, 3, 3, 5)

print(l)

for i in None:
  print(i)

print("out of loop")