from intcode import Intcode

with open('inputs/day17.in') as f:
    data = f.read().strip()

comp = Intcode(data, [])
comp.run()
print(comp.outputs)
map_ = ''.join([chr(o) for o in comp.outputs])
print(map_)
grid = map_.strip().split('\n')
total = 0
for r in range(1, len(grid)-1):
    if(len(grid[r])) > 0:
        for c in range(1, len(grid[0]) - 1):
            if grid[r][c] == '#' and grid[r-1][c] == '#' and grid[r+1][c] == '#' \
                and grid[r][c-1] == '#' and grid[r][c+1] == '#':
                    total += r*c

print(total)