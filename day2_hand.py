import time
start = time.time()

with open('inputs/day2.in') as f:
    data = [int(x) for x in f.read().split(',')]

def get_output(n, v):
    return 384000* n + v + 490656

ans1 = get_output(12, 2)

target = 19690720

for n in range(100):
    v = target - 490656 - 384000 * n
    if 0 < v < 100:
        ans2 = v
        break

end = time.time()
print('Part 1', ans1)
print('Part 2', n*100 + ans2)
print((end - start))
