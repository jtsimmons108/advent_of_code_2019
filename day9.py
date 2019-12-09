from intcode import Intcode
with open('inputs/day9.in') as f:
    instructions = f.read().strip()


comp = Intcode(instructions, [1])
ans1 = comp.run()

comp = Intcode(instructions, [2])
ans2 = comp.run()
print(ans1, ans2)