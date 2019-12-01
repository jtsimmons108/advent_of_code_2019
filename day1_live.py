with open('inputs/day1.in') as f:
    inpt = f.read()

data = inpt.strip().split('\n')

total = 0

for line in data:
    num = int(line) // 3 - 2
    while num > 0:
        total += num
        num = num // 3 - 2
    
print(total)
