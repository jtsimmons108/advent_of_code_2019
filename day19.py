from intcode import Intcode

with open('inputs/day19.in') as f:
    data = f.read().strip()

def get_grid_point(x, y):
    comp = Intcode(data, [x,y])
    comp.run()
    return comp.outputs[-1]

total = 0
for x in range(50):
    for y in range(50):
        total += get_grid_point(x,y)

print(total)
x, y = 106, 105
found = False
print(get_grid_point(206, 205))
    
print(x,y)
