from collections import defaultdict
with open('inputs/day14.in') as f:
    data = f.read().strip().split('\n')

requirements = {}
def split_input(inpt):
    amt, el = inpt.split()
    return int(amt), el
def produced_by_ore(el):
    return len(requirements[el][0]) == 1 and requirements[el][0][0][1] == 'ORE'

def get_requirements(el, total):
    print('finding reqs for', total, el)
    reqs,  amt = requirements[el]
    all_reqs = []
    for num, r in reqs:
        if produced_by_ore(r):
            all_reqs.append((num * amt * total, r))
        else:
            all_reqs.extend(get_requirements(r, amt*num*total))
    return all_reqs

def get_ore_amount(el, needed):
    lst, num = requirements[el]
    ore = lst[0][0]
    total = needed // num
    if needed % num != 0:
        total += 1
    return total * ore
for line in data:
    inpt, outpt = line.split(' => ')
    inpt = [split_input(ind) for ind in inpt.split(', ')]
    amt, el  = split_input(outpt)
    requirements[el] = inpt, amt


reqs = get_requirements('FUEL', 1)
print(reqs)
final = defaultdict(int)

for num, el in reqs:
    final[el] += num

ore = 0
for el, num in final.items():
    ore += get_ore_amount(el, num)

print(ore)
