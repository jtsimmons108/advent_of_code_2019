from intcode import Intcode
import threading, itertools

with open('inputs/day7.in') as f:
    data = f.read().strip()

def supply_thrusters(phases):
    amps = [Intcode(data, [a]) for a in phases]
    amps[0].inputs.append(0)

    for i in range(-1, len(amps)-1):
        amps[i].set_link(amps[i+1])

    threads = [threading.Thread(target=amp.run) for amp in amps]

    for thread in threads:
        thread.start()
        thread.join()
    return amps[-1].outputs[-1]


