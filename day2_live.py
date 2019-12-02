with open('inputs/day2.in') as f:
    inpt = f.read()

data = inpt.strip().split(',')
nums = list(map(int, data))

index = 0
for noun in range(100):
    for verb in range(100):
        index = 0
        vals = nums[::]
        vals[1] = noun
        vals[2] = verb
        while True:
            if vals[index] == 1:
                vals[vals[index + 3]] = vals[vals[index + 1]] + vals[vals[index + 2]]
            elif vals[index] == 2:
                vals[vals[index + 3]]= vals[vals[index + 1]] * vals[vals[index + 2]]
            elif vals[index] == 99:
                break
            
            index += 4
        if vals[0] == 19690720:
            print(noun, verb)

