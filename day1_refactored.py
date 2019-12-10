def get_fuel(num):
    return num // 3 - 2

def get_total_fuel(num):
    total = 0
    num = get_fuel(num)
    while num > 0:
        total += num
        num = get_fuel(num)
    return total

with open('inputs/day1.in') as f:
    inpt = f.read()

data = inpt.strip().split('\n')
print('Part 1:', sum(get_fuel(int(num)) for num in data))
print('Part 2:', sum(get_total_fuel(int(num)) for num in data))