with open('inputs/day1.in') as f:
    nums = [int(x) for x in f.read().split('\n')]

total = 0

while len(nums) > 0:
    nums = [mass // 3 - 2 for mass in nums if mass >= 9]
    total += sum(nums)

print(total)