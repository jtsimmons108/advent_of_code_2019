with open('inputs/day5.in') as f:
    instructions = [int(num) for num in f.read().strip().split(',')]


index = 0

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

while instructions[index] != 99:
    opcode = instructions[index] % 100
    if opcode in [1,2,7,8]:
        op, reg1, reg2, reg3 = instructions[index:index + 4]
        param2, param1, op = get_split_instruction(op)
        if op == 1:
            result = get_value(instructions, param1, reg1) + get_value(instructions, param2, reg2)
        elif op == 2:
            result = get_value(instructions, param1, reg1) * get_value(instructions, param2, reg2)
        elif op == 7:
            if get_value(instructions, param1, reg1) < get_value(instructions, param2, reg2):
                result = 1
            else:
                result = 0
        elif op == 8:
            if get_value(instructions, param1, reg1) == get_value(instructions, param2, reg2):
                result = 1
            else:
                result = 0
        instructions[reg3] = result
        index += 4
    elif opcode in [3,4]:
        op, reg = instructions[index:index + 2]
        param1, op = get_split_instruction(op)
        if op == 3:
            instructions[reg] = int(input('Enter value: '))
        elif op == 4:
            print(instructions[reg])

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
        
