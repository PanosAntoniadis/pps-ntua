import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

tp_1 = []
tp_2 = []

threads = ['1', '2', '4', '8', '16', '32', '64']

fp = open(sys.argv[1])
line = fp.readline()
while line:
    if line.startswith("MT_CONF="):
        line = fp.readline()
        continue
    tokens = line.split()
    tp_1.append(float(tokens[5]))
    line = fp.readline()
fp.close()

fp = open(sys.argv[2])
line = fp.readline()
while line:
    if line.startswith("MT_CONF="):
        line = fp.readline()
        continue
    tokens = line.split()
    tp_2.append(float(tokens[5]))
    line = fp.readline()
fp.close()

print(tp_1)
print(tp_2)


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of threads")

ax.xaxis.set_ticks(np.arange(0, len(threads), 1))
ax.set_xticklabels(threads, rotation=45)
ax.set_xlim(-0.5, len(threads) - 0.5)
ax.set_ylabel("Throughput(Mops/sec)")

ax.plot(tp_1, label="1st execution", color="blue", marker='x')
ax.plot(tp_2, label="2nd execution", color="red", marker='x')


plt.title("Throughput for different executions")
lgd = plt.legend(['1st execution', '2nd execution'])

lgd.draw_frame(False)
plt.savefig("ex1_thoughput.png", bbox_inches="tight")
