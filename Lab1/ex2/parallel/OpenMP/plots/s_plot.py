import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

time = []
cores = ['1', '2', '4', '8', '16', '32', '64']


fp = open(sys.argv[1])
line = fp.readline()
while line:
    tokens = line.split(',')
    time.append(float(tokens[2]))
    line = fp.readline()
fp.close()


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of cores")

ax.xaxis.set_ticks(np.arange(0, len(cores), 1))
ax.set_xticklabels(cores, rotation=45)
ax.set_xlim(-0.5, len(cores) - 0.5)
ax.set_ylabel("time")

ax.plot(time, label="Time", color="blue", marker='x')

plt.title("Parallel for in FW algorithm in 4096×4096")
lgd = plt.legend(['standard FW'])
lgd.draw_frame(False)
plt.savefig("s_4096.png", bbox_inches="tight")
