with open('inputs/day8.in') as f:
    data = [int(c) for c in f.read().strip()]

layers = [data[i:i+150] for i in range(0, len(data), 150)]
least = min(layers, key = lambda layer: layer.count(0))
print(least.count(1) * least.count(2))

pixels = [next(filter(lambda p: p != 2, stack)) for stack in zip(*layers)]
image = [pixels[i: i + 25] for i in range(0, len(pixels), 25)]
for row in image:
    print(''.join(['█' if p == 1 else ' ' for p in row]))