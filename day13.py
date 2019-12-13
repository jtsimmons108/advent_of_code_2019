from intcode import Intcode

with open('inputs/day13.in') as f:
    data = f.read().strip()


comp = Intcode(data,[])
comp.run()
print(comp.outputs[2::3].count(2))
