from random import randint

randomlist = []
doublelist = []

for l in range(0, 10):
  randomlist.append(randint(1, 10))

print(randomlist)

thesumm = sum(randomlist)
arr = thesumm / len(randomlist)
print(arr)

if arr >= 5:
  print(randomlist[::-1])
elif arr < 5:
  for x in randomlist:
    double = x * 2
    doublelist.append(double)
  print(doublelist)





