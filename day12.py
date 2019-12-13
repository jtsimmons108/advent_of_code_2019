from math import gcd
import re
with open('inputs/day12.in') as f:
    data = f.read().strip().split('\n')

def lcm(nums):
    lcm = nums[0]
    for num in nums[1:]:
        lcm = lcm*num//gcd(lcm, num)
    return lcm

def update_positions(axis, vels):
    num = len(axis)
    for i in range(num):
        for j in range(num):
            vels[i] += 1 * (axis[i] < axis[j])
            vels[i] += -1 * (axis[i] > axis[j])
    for i in range(num):
        axis[i] += vels[i]

def find_cycle(axis):
    start = axis[:]
    vels = [0] * len(axis)
    steps = 1
    update_positions(axis, vels)
    while start != axis or vels != [0,0,0,0]:
        update_positions(axis, vels)
        steps += 1

    return steps
    

planets = [list(map(int, re.findall(r'-?\d+', line))) for line in data]
axes = [list(axis) for axis in zip(*planets)]
vels = [[0 for _ in range(len(axes[0]))] for axis in axes]

axes2 = [axis[:] for axis in axes]

for i in range(len(axes)):
    for _ in range(1000):
        update_positions(axes[i], vels[i])

total = 0
positions = list(zip(*axes))
velocities = list(zip(*vels))
for i in range(len(positions)):
    total += sum(map(abs, positions[i])) * sum(map(abs, velocities[i]))
print(total)
print(lcm([find_cycle(axis) for axis in axes2]))



