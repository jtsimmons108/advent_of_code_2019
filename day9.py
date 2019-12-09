from intcode import Intcode
with open('inputs/day9.in') as f:
    instructions = f.read().strip()

comp = Intcode(instructions, [2])
comp.run()