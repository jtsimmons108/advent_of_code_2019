from intcode import Intcode

with open('inputs/day13.in') as f:
    data = f.read().strip()

bx, by = 0,0
px, py = 0,0
comp = Intcode(data,[])
comp.codes[0] = 2
score = 0
while not comp.halted:
    comp.run()

    for i in range(0,len(comp.outputs),3):
        x, y, tile = comp.outputs[i:i+3]
        if tile > 4:
            score = tile
        elif tile == 4:
            bx, by = x, y
        elif tile == 3:
            px, py = x, y
        
    comp.outputs = []
    if bx > px:
        joystick = 1
    elif bx < px:
        joystick = -1
    else:
        joystick = 0
    comp.inputs.append(joystick)

print(score)
