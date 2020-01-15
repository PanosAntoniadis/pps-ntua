import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

fgl_1024 = []
fgl_8192 = []

opt_1024 = []
opt_8192 = []

lazy_1024 = []
lazy_8192 = []

threads = ['1', '2', '4', '8', '16', '32', '64']

for filename in sys.argv[1:]:
    type = filename.split('/')[-1].split('_')[1]
    fp = open(filename, 'r')
    line = fp.readline()
    i = 0
    while line:
        if line.startswith("MT_CONF="):
            line = fp.readline()
            continue
        tokens = line.split()
        if i < 7:
            if type == 'fgl':
                fgl_1024.append(float(tokens[7]))
            if type == 'opt':
                opt_1024.append(float(tokens[7]))
            if type == 'lazy':
                lazy_1024.append(float(tokens[7]))
        elif i < 14:
            if type == 'fgl':
                fgl_8192.append(float(tokens[7]))
            if type == 'opt':
                opt_8192.append(float(tokens[7]))
            if type == 'lazy':
                lazy_8192.append(float(tokens[7]))
        line = fp.readline()
        i += 1
    fp.close()


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of threads")

ax.xaxis.set_ticks(np.arange(0, len(threads), 1))
ax.set_xticklabels(threads, rotation=45)
ax.set_xlim(-0.5, len(threads) - 0.5)
ax.set_ylabel("Throughput(Mops/sec)")

ax.plot(fgl_1024, label="fgl", color="blue", marker='x')
ax.plot(opt_1024, label="opt", color="red", marker='x')
ax.plot(lazy_1024, label="lazy", color="black", marker='x')


plt.title("Throughput for Size: 1024 and Workload: 20/40/40")
lgd = plt.legend()

lgd.draw_frame(False)
plt.savefig("ex3_thoughput_1024_2.png", bbox_inches="tight")


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of threads")

ax.xaxis.set_ticks(np.arange(0, len(threads), 1))
ax.set_xticklabels(threads, rotation=45)
ax.set_xlim(-0.5, len(threads) - 0.5)
ax.set_ylabel("Throughput(Mops/sec)")

ax.plot(fgl_8192, label="fgl", color="blue", marker='x')
ax.plot(opt_8192, label="opt", color="red", marker='x')
ax.plot(lazy_8192, label="lazy", color="black", marker='x')


plt.title("Throughput for Size: 8192 and Workload: Workload: 20/40/40")
lgd = plt.legend()

lgd.draw_frame(False)
plt.savefig("ex3_thoughput_8192_2.png", bbox_inches="tight")
