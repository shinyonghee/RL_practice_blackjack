from env import step, reset
import numpy as np

# hyper parameters
gamma = 1
# dealer * player
Q = np.zeros((21, 21, 2))

s = reset()
memory = []
num_epoch = 10
for i in range(num_epoch):

    while s != "terminal":
        # STICK: 0, HIT: 1
        a = np.argmax(Q[s])
        s, r = step(s, a)
        memory.append((s, a, r))
        print((s, a, r))
    for j in reversed(memory):
        s = j[0]
        a = j[1]
        r = j[2]
