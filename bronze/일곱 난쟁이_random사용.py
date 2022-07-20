import random
height = []
s =[]
for i in range(9):
    height.append(int(input()))

while True:
    real = random.sample(height,7)
    if sum(real) == 100:
      s = sorted(real)
      break

for k in s:
  print(k)