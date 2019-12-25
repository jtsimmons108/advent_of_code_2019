with open('inputs/day24.in') as f:
    grid = [line for line in f.read().strip().split('\n')]

seen = set()

def get_grid_string(grid):
    return ''.join([''.join(row) for row in grid])

def get_biodiversity_rating(grid):
    total = 0
    for r in range(5):
        for c in range(5):
            if grid[r][c] == '#':
                total += 2**(5 * r + c)

    return total
def is_bug(grid, r, c):
    return int(grid[r][c] == '#')

def get_neighbor_count(grid, r, c):
    total = 0
    if c > 0:
        total += is_bug(grid, r, c-1)
    if c < 4:
        total += is_bug(grid, r, c+1)
    if r > 0:
        total += is_bug(grid, r-1, c)
    if r < 4:
        total += is_bug(grid, r+1, c)
    return total

def get_next_grid(grid):
    new_grid = [['' for _ in range(5)] for _ in range(5)]
    for r in range(5):
        for c in range(5):
            if is_bug(grid, r, c):
                new_grid[r][c] = '#' if get_neighbor_count(grid, r, c) == 1 else '.'
            else:
                count = get_neighbor_count(grid, r, c)
                new_grid[r][c] = '#' if count == 1 or count == 2 else '.'
    return new_grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print('\n\n')

grid_string = get_grid_string(grid)
while grid_string not in seen:
    seen.add(grid_string)
    grid = get_next_grid(grid)
    grid_string = get_grid_string(grid)

print(get_biodiversity_rating(grid))