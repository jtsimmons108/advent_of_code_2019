from math import gcd, atan2, degrees
from collections import defaultdict

with open('inputs/day10.in') as f:
    data = [[c for c in line] for line in f.read().strip().split('\n')]


asteroids = set()

for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == '#':
            asteroids.add((c, r))

def manhattan_distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def get_see_count(ast):
    gradients = set()
    for ast2 in asteroids:
        dx, dy = ast2[0] - ast[0], ast[1] - ast2[1]
        g = gcd(abs(dx), abs(dy))
        if g != 0:
            gradients.add((dx//g, dy//g))
    return len(gradients)

def degrees_from_tower(ast):
    deg = degrees(atan2(tower[1] - ast[1], ast[0] - tower[0]))
    deg = (deg + 360) % 360
    return (-deg + 90) % 360

tower = max(asteroids, key=lambda ast: get_see_count(ast))
print(get_see_count(tower))

atans = defaultdict(list)
for ast in asteroids:
    if ast != tower:
        atans[degrees_from_tower(ast)].append(ast)


for deg in atans:
    atans[deg].sort(key=lambda p: manhattan_distance(p, tower))

ordered = sorted(atans.items(), key=lambda item: item[0])

destroyed = []
while len(destroyed) != len(asteroids) - 1:
    for deg, ast_list in ordered:
        if len(ast_list) != 0:
            destroyed.append(ast_list.pop(0))

x, y = destroyed[199]
print(x*100+y)