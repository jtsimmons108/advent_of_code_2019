with open('inputs/day8.in') as f:
    data = [int(c) for c in f.read().strip()]

rows, cols = 6, 25
layer_length = rows * cols
layers = [data[i:i+layer_length] for i in range(0, len(data), layer_length)]


least = min(layers, key = lambda layer: layer.count(0))
print(least.count(1) * least.count(2))

image = [[2 for _ in range(cols)] for _ in range(rows)]

for layer in layers:
    for i in range(layer_length):
        r, c = i // cols, i % cols
        if image[r][c] == 2:
            image[r][c] = layer[i]

for row in image:
    print(''.join(['*' if pixel == 1 else ' ' for pixel in row]))