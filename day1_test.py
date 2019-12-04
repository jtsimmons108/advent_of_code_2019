with open('inputs/day1.in') as f:
    nums = [int(x) for x in f.read().split('\n')]

fuels = [num // 3 - 2 for num in nums]
total = sum(fuels)
print(total)

while len(fuels) > 0:
    fuels = [fuel // 3 - 2 for fuel in fuels if fuel >= 9]
    print(fuels)
    total += sum(fuels)
print(total)

