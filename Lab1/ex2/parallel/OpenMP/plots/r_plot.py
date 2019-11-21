import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

time = []
cores = ['1', '2', '4', '8', '16', '32', '64']

for out_file in sys.argv[1:]:
    fp = open(out_file)
    time_i = []
    line = fp.readline()
    while line:
        tokens = line.split(',')
        time_i.append(float(tokens[3]))
        line = fp.readline()
    fp.close()
    time.append(time_i)


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of cores")

ax.xaxis.set_ticks(np.arange(0, len(cores), 1))
ax.set_xticklabels(cores, rotation=45)
ax.set_xlim(-0.5, len(cores) - 0.5)
ax.set_ylabel("time")

ax.plot(time[0], label="Time", color="blue", marker='x')


plt.title("Task based parallelization of recursive FW algorithm in 4096×4096")
lgd = plt.legend(['recursive - B=256'])
lgd.draw_frame(False)
plt.savefig("r_4096.png", bbox_inches="tight")
