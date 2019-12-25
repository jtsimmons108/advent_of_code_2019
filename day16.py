with open('inputs/day16.in') as f:
    signal = [int(dig) for dig in f.read().strip()*4]

sequence = (0,1,0,-1)


def apply_fft(signal):
    new_sigs = []
    for i in range(len(signal)):
        result = 0
        j = 1
        for sig in signal:
            result += sig * sequence[j//(i + 1) % 4]
            j+= 1
        new_sigs.append(int(str(result)[-1]))

    return new_sigs


for _ in range(100):
    signal = apply_fft(signal)

print(''.join(str(s) for s in signal[:8]))


