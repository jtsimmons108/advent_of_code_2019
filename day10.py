from math import gcd
with open('inputs/day10.in') as f:
    data = [[c for c in line] for line in f.read().strip().split('\n')]

asteroids = set()

for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == '#':
            asteroids.add((c, r))

def can_be_blocked(ast1, ast2):
    dx, dy = abs(ast2[0] - ast1[0]), abs(ast2[1] - ast1[1])
    return gcd(dx, dy) != 1

def get_blockers(ast1, ast2):
    dx, dy = ast2[0] - ast1[0], ast2[1] - ast1[1]
    x, y = ast1
    steps = max(abs(dx), abs(dy)) if dx == 0 or dy == 0 else gcd(abs(dx), abs(dy))

    return [(x + step * dx // steps, y + step * dy // steps) for step in range(1, steps)]
def can_see(ast1, ast2):
    if ast1 == ast2:
        return False
    if not can_be_blocked(ast1, ast2):
        return True
    return not any(ast in asteroids for ast in get_blockers(ast1, ast2))
    

views = {}

for ast in asteroids:
    views[ast] = sum([can_see(ast, other) for other in asteroids])

print(max(views.items(), key = lambda item: item[1]))