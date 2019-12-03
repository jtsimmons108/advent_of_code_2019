import re, itertools, numpy as np
from collections import deque, defaultdict

with open('inputs/day3.in') as f:
    inpt = f.read()

# with open('inputs/test.in') as f:
#     inpt = f.read()

path1, path2 = inpt.strip().split('\n')
deltas = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
p1_points = set()
p2_points = set()

def find_points(points, directions):
    curr_x, curr_y = 0, 0
    directions = directions.split(',')
    for dir in directions:
        d, l = dir[:1], int(dir[1:])
        dx, dy = deltas[d]
        for _ in range(l):
            curr_x += dx
            curr_y += dy
            points.add((curr_x, curr_y))


def find_intersection_steps(points, directions, intersections):
    step_counts = {}
    curr_x, curr_y = 0, 0
    directions = directions.split(',')
    steps = 0
    for dir in directions:
        d, l = dir[:1], int(dir[1:])
        dx, dy = deltas[d]
        for _ in range(l):
            curr_x += dx
            curr_y += dy
            steps += 1
            if (curr_x, curr_y) in intersections and (curr_x, curr_y) not in points:
                step_counts[(curr_x, curr_y)] = steps
            else:
                points.add((curr_x, curr_y))
    print(step_counts)
    return step_counts




find_points(p1_points, path1)
find_points(p2_points, path2)

dist = []
intersections = p1_points & p2_points
print(intersections)
for x, y in intersections:
    dist.append(abs(x) + abs(y))

print(min(dist))


p1_points = set()
p2_points = set()

p1_intersections = find_intersection_steps(p1_points, path1, intersections)
p2_intersections = find_intersection_steps(p2_points, path2, intersections)

print(min([p1_intersections[key] + p2_intersections[key] for key in p1_intersections]))




        

    