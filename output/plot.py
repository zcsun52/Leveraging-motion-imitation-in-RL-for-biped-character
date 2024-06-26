import numpy as np
import matplotlib.pyplot as plt

# with open("agent0_log.txt") as f:
#     lines = f.readlines()
#     x = [line.split()[0] for line in lines]
#     y = [line.split()[3] for line in lines]
data = np.loadtxt('agent0_log.txt')
it = data[:,0]
rew = data[:, 3]
plt.plot(it, rew,'r--')
plt.show()