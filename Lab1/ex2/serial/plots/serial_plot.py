import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

time = []
cores = ['16', '32', '64', '128', '265', '512']

time_r = []
for out_file in sys.argv[1:7]:
    fp = open(out_file)
    for i, line in enumerate(fp):
        if i == 2:
            tokens = line.split(',')
            time_r.append(float(tokens[3]))
    fp.close()

time_t = []
for out_file in sys.argv[7:]:
    fp = open(out_file)
    for i, line in enumerate(fp):
        if i == 0:
            tokens = line.split(',')
            time_t.append(float(tokens[3]))
    fp.close()


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("block size")

ax.xaxis.set_ticks(np.arange(0, len(cores), 1))
ax.set_xticklabels(cores, rotation=45)
ax.set_xlim(-0.5, len(cores) - 0.5)
ax.set_ylabel("time")

ax.plot(time_r, label="Time", color="blue", marker='x')
ax.plot(time_t, label="Time", color="red", marker='x')


plt.title("Time of FW based on block size in 4096×4096")
lgd = plt.legend(['recursive', 'tiled'])
lgd.draw_frame(False)
plt.savefig("s_4096.png", bbox_inches="tight")
