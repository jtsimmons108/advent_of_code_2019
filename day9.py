from intcode import Intcode
with open('inputs/day9.in') as f:
    instructions = f.read().strip()


comp = Intcode(instructions, [1])
print(comp.run())

comp = Intcode(instructions, [2])
print(comp.run())
