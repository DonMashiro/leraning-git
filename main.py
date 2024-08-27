numbers = list(range(0, 101))
numbers_5 = []
for number in numbers:
  if number % 5 == 0:
    numbers_5.append(number)
print(numbers_5)
cube = [number **3 for number in numbers_5]
print(cube)
