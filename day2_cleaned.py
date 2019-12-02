with open('inputs/day2.in') as f:
    inpt = f.read()


intcodes = list(map(int, inpt.split(',')))

def get_output(intcodes, noun, verb):
    nums = intcodes[::]
    nums[1] = noun
    nums[2] = verb
    index = 0
    while nums[index] != 99:
        op, pos1, pos2, store_pos = nums[index:index + 4]
        if op == 1:
            result = nums[pos1] + nums[pos2]
        else:
            result = nums[pos1] * nums[pos2]
        
        nums[store_pos] = result
        index += 4

    return nums[0]

print('Part 1:', get_output(intcodes, 12, 2))

target = 19690720
for noun in range(100):
    for verb in range(100):
        if get_output(intcodes, noun, verb) == target:
            print('Part 2:', noun * 100 + verb)


