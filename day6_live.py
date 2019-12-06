from collections import defaultdict


with open('inputs/day6.in') as f:
    data = f.read().strip().split('\n')


orbits = {}
children = defaultdict(list)
for line in data:
    a, b = line.split(')')
    orbits[b] = a
    children[a].append(b)

def get_orbit_count(planet):
    if planet not in orbits:
        return 0
    return 1 + get_orbit_count(orbits[planet])

def has_santa(planet):
    if planet not in children:
        return False
    if 'SAN' in children[planet]:
        return True
    return any(has_santa(child) for child in children[planet])

def get_hops_to_santa(planet):
    if 'SAN' in children[planet]:
        return 

def get_hops_to_santa(parent):
    hops = 0
    while not has_santa(parent):
        hops += 1
        parent = orbits[parent]
    while 'SAN' not in children[parent]:
        hops += 1
        for child in children[parent]:
            if has_santa(child):
                parent = child
                continue
    return hops


print(sum([get_orbit_count(planet) for planet in orbits]))
print(get_hops_to_santa(orbits['YOU']))