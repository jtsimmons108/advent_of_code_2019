from intcode import Intcode

with open('inputs/day5.in') as f:
    data = f.read().strip()

comp = Intcode(data, [1])
print(comp.run())

comp = Intcode(data, [5])
print(comp.run())