import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

t_64 = []
t_1024 = []
t_4096 = []

s_64 = []
s_1024 = []
s_4096 = []

fp = open(sys.argv[1])
line = fp.readline()
while line:
    tokens = line.split()
    if tokens[2] == '64':
        t_64.append(float(tokens[6]) * 100)
    if tokens[2] == '1024':
        t_1024.append(float(tokens[6]))
    if tokens[2] == '4096':
        t_4096.append(float(tokens[6]))
    line = fp.readline()

fp.close()

print(t_64)
print(t_1024)
print(t_4096)

for i in range(0, len(t_64)):
    s_64.append(t_64[0] / t_64[i])
    s_1024.append(t_1024[0] / t_1024[i])
    s_4096.append(t_4096[0] / t_4096[i])

print(s_64)
print(s_1024)
print(s_4096)

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of cores")
ax.xaxis.set_ticks(np.arange(0, 5, 1))
ax.set_xticklabels(['1', '2', '4', '6', '8'], rotation=45)
ax.set_xlim(-0.5, 4.5)
ax.set_ylabel("time (ms)")
plt.plot(t_64, label="Time", color="blue", marker='x')
plt.title("Game of Life in 64×64 table")
plt.savefig("time_64.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of cores")
ax.xaxis.set_ticks(np.arange(0, 5, 1))
ax.set_xticklabels(['1', '2', '4', '6', '8'], rotation=45)
ax.set_xlim(-0.5, 4.5)
ax.set_ylabel("time (s)")
plt.plot(t_1024, label="Time", color="blue", marker='x')
plt.title("Game of Life 1024×1024 table")
plt.savefig("time_1024.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of cores")
ax.xaxis.set_ticks(np.arange(0, 5, 1))
ax.set_xticklabels(['1', '2', '4', '6', '8'], rotation=45)
ax.set_xlim(-0.5, 4.5)
ax.set_ylabel("time (s)")
plt.plot(t_4096, label="Time", color="blue", marker='x')
plt.title("Game of Life 4096×4096 table")
plt.savefig("time_4096.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of cores")
ax.xaxis.set_ticks(np.arange(0, 5, 1))
ax.set_xticklabels(['1', '2', '4', '6', '8'], rotation=45)
ax.set_xlim(-0.5, 4.5)
ax.set_ylabel("speedup")
plt.plot(s_64, label="Speedup", color="blue", marker='x')
plt.title("Game of Life in 64×64 table")
plt.savefig("speedup_64.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of cores")
ax.xaxis.set_ticks(np.arange(0, 5, 1))
ax.set_xticklabels(['1', '2', '4', '6', '8'], rotation=45)
ax.set_xlim(-0.5, 4.5)
ax.set_ylabel("speedup")
plt.plot(s_1024, label="Speedup", color="blue", marker='x')
plt.title("Game of Life 1024×1024 table")
plt.savefig("speedup_1024.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of cores")
ax.xaxis.set_ticks(np.arange(0, 5, 1))
ax.set_xticklabels(['1', '2', '4', '6', '8'], rotation=45)
ax.set_xlim(-0.5, 4.5)
ax.set_ylabel("speedup")
plt.plot(s_4096, label="Speedup", color="blue", marker='x')
plt.title("Game of Life 4096×4096 table")
plt.savefig("speedup_4096.png", bbox_inches="tight")
