import itertools
def get_value(instructions, param, val):
    if param == 0:
        return instructions[val]
    return val

def get_split_instruction(opcode):
    op = opcode % 100
    if op in [1,2,5,6,7,8]:
        op = '{:04}'.format(opcode)
        return int(op[0]), int(op[1]), int(op[2:])
    elif op in [3,4]:
        op = '{:03}'.format(opcode)
        return int(op[0]), int(op[1:])

def run_instructions(amp):
    instructions, index, inputs, outputs, halted = amp
   
    while instructions[index] != 99:
        opcode = instructions[index] % 100
        if opcode in [1,2,7,8]:
            op, reg1, reg2, reg3 = instructions[index:index + 4]
            param2, param1, op = get_split_instruction(op)
            first = get_value(instructions, param1, reg1)
            second = get_value(instructions, param2, reg2)
            if op == 1:
                result = get_value(instructions, param1, reg1) + get_value(instructions, param2, reg2)
            elif op == 2:
                result = get_value(instructions, param1, reg1) * get_value(instructions, param2, reg2)
            elif op == 7:
                result = int(get_value(instructions, param1, reg1) < get_value(instructions, param2, reg2))
            elif op == 8:
                result = int(get_value(instructions, param1, reg1) == get_value(instructions, param2, reg2))
            instructions[reg3] = result
            index += 4
        elif opcode in [3,4]:
            op, reg = instructions[index:index + 2]
            param1, op = get_split_instruction(op)
            if op == 3:
                if len(inputs) > 0:
                    instructions[reg] = inputs.pop(0)
                else:
                    return
            elif op == 4:
                result = get_value(instructions, param1, reg)
                if result != 0:
                    outputs.append(result)
                    amp[1] = index + 2
                    return result

            index += 2
        elif opcode in [5,6]:
            op, reg1, reg2 = instructions[index:index + 3]
            param2, param1, op = get_split_instruction(op)
            if op == 5:
                if get_value(instructions, param1, reg1) != 0:
                    index = get_value(instructions, param2, reg2)
                else:
                    index += 3
            else:
                if get_value(instructions, param1, reg1) == 0:
                    index = get_value(instructions, param2, reg2)
                else:
                    index += 3
    amp[-1] = True

    
with open('inputs/day7.in') as f:
    data = [int(num) for num in f.read().strip().split(',')]

signals = []

for a,b,c,d,e in itertools.permutations((9,7,8,5,6)):
    amp_a = [data[:], 0, [a,0], [], False]
    amp_b = [data[:], 0, [b], [], False]
    amp_c = [data[:], 0, [c], [], False]
    amp_d = [data[:], 0, [d], [], False]
    amp_e = [data[:], 0, [e], [], False]

    amps = (amp_a, amp_b, amp_c, amp_d, amp_e)

    amp = 0
    while not amps[-1][-1]:
        output = run_instructions(amps[amp])
        next_ = (amp + 1) % len(amps)
        if output != None:
            amps[next_][2].append(output)
        else:
            break
        amp = next_
    try:
        signals.append(amps[-1][-2][-1])
    except:
        pass

print(max(signals))