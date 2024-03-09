# loops.py

## while loop
i = 1
while i < 6:
  print(i)
  i += 1

## for loop
for i in range(6):
  print(i)

## nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
