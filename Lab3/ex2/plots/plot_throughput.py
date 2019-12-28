import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

nosync_16 = []
nosync_1024 = []
nosync_8192 = []

pthread_16 = []
pthread_1024 = []
pthread_8192 = []

tas_16 = []
tas_1024 = []
tas_8192 = []

ttas_16 = []
ttas_1024 = []
ttas_8192 = []

array_16 = []
array_1024 = []
array_8192 = []

clh_16 = []
clh_1024 = []
clh_8192 = []

threads = ['1', '2', '4', '8', '16', '32', '64']

for filename in sys.argv[1:]:
    type = filename.split('/')[-1].split('_')[1].split('.')[0]
    fp = open(filename, 'r')
    line = fp.readline()
    i = 0
    while line:
        if line.startswith("MT_CONF="):
            line = fp.readline()
            continue
        tokens = line.split()
        if i < 7:
            if type == 'nosync':
                nosync_16.append(float(tokens[5]))
            if type == 'pthread':
                pthread_16.append(float(tokens[5]))
            if type == 'tas':
                tas_16.append(float(tokens[5]))
            if type == 'ttas':
                ttas_16.append(float(tokens[5]))
            if type == 'array':
                array_16.append(float(tokens[5]))
            if type == 'clh':
                clh_16.append(float(tokens[5]))
        elif i < 14:
            if type == 'nosync':
                nosync_1024.append(float(tokens[5]))
            if type == 'pthread':
                pthread_1024.append(float(tokens[5]))
            if type == 'tas':
                tas_1024.append(float(tokens[5]))
            if type == 'ttas':
                ttas_1024.append(float(tokens[5]))
            if type == 'array':
                array_1024.append(float(tokens[5]))
            if type == 'clh':
                clh_1024.append(float(tokens[5]))
        else:
            if type == 'nosync':
                nosync_8192.append(float(tokens[5]))
            if type == 'pthread':
                pthread_8192.append(float(tokens[5]))
            if type == 'tas':
                tas_8192.append(float(tokens[5]))
            if type == 'ttas':
                ttas_8192.append(float(tokens[5]))
            if type == 'array':
                array_8192.append(float(tokens[5]))
            if type == 'clh':
                clh_8192.append(float(tokens[5]))
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

ax.plot(nosync_16, label="nosync lock", color="blue", marker='x')
ax.plot(pthread_16, label="pthread lock", color="red", marker='x')
ax.plot(tas_16, label="tas lock", color="black", marker='x')
ax.plot(ttas_16, label="ttas lock", color="green", marker='x')
ax.plot(array_16, label="array lock", color="orange", marker='x')
ax.plot(clh_16, label="clh lock", color="grey", marker='x')


plt.title("Throughput for size=16")
lgd = plt.legend()

lgd.draw_frame(False)
plt.savefig("ex2_thoughput_16.png", bbox_inches="tight")


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of threads")

ax.xaxis.set_ticks(np.arange(0, len(threads), 1))
ax.set_xticklabels(threads, rotation=45)
ax.set_xlim(-0.5, len(threads) - 0.5)
ax.set_ylabel("Throughput(Mops/sec)")

ax.plot(nosync_1024, label="nosync lock", color="blue", marker='x')
ax.plot(pthread_1024, label="pthread lock", color="red", marker='x')
ax.plot(tas_1024, label="tas lock", color="black", marker='x')
ax.plot(ttas_1024, label="ttas lock", color="green", marker='x')
ax.plot(array_1024, label="array lock", color="orange", marker='x')
ax.plot(clh_1024, label="clh lock", color="grey", marker='x')


plt.title("Throughput for size=1024")
lgd = plt.legend()

lgd.draw_frame(False)
plt.savefig("ex2_thoughput_1024.png", bbox_inches="tight")


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of threads")

ax.xaxis.set_ticks(np.arange(0, len(threads), 1))
ax.set_xticklabels(threads, rotation=45)
ax.set_xlim(-0.5, len(threads) - 0.5)
ax.set_ylabel("Throughput(Mops/sec)")

ax.plot(nosync_8192, label="nosync lock", color="blue", marker='x')
ax.plot(pthread_8192, label="pthread lock", color="red", marker='x')
ax.plot(tas_8192, label="tas lock", color="black", marker='x')
ax.plot(ttas_8192, label="ttas lock", color="green", marker='x')
ax.plot(array_8192, label="array lock", color="orange", marker='x')
ax.plot(clh_8192, label="clh lock", color="grey", marker='x')


plt.title("Throughput for size=8192")
lgd = plt.legend()

lgd.draw_frame(False)
plt.savefig("ex2_thoughput_8192.png", bbox_inches="tight")


########################
# Plots without nosync #
########################

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of threads")

ax.xaxis.set_ticks(np.arange(0, len(threads), 1))
ax.set_xticklabels(threads, rotation=45)
ax.set_xlim(-0.5, len(threads) - 0.5)
ax.set_ylabel("Throughput(Mops/sec)")

ax.plot(pthread_16, label="pthread lock", color="red", marker='x')
ax.plot(tas_16, label="tas lock", color="black", marker='x')
ax.plot(ttas_16, label="ttas lock", color="green", marker='x')
ax.plot(array_16, label="array lock", color="orange", marker='x')
ax.plot(clh_16, label="clh lock", color="grey", marker='x')


plt.title("Throughput for size=16")
lgd = plt.legend()

lgd.draw_frame(False)
plt.savefig("ex2_thoughput_16_sync.png", bbox_inches="tight")


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of threads")

ax.xaxis.set_ticks(np.arange(0, len(threads), 1))
ax.set_xticklabels(threads, rotation=45)
ax.set_xlim(-0.5, len(threads) - 0.5)
ax.set_ylabel("Throughput(Mops/sec)")

ax.plot(pthread_1024, label="pthread lock", color="red", marker='x')
ax.plot(tas_1024, label="tas lock", color="black", marker='x')
ax.plot(ttas_1024, label="ttas lock", color="green", marker='x')
ax.plot(array_1024, label="array lock", color="orange", marker='x')
ax.plot(clh_1024, label="clh lock", color="grey", marker='x')


plt.title("Throughput for size=1024")
lgd = plt.legend()

lgd.draw_frame(False)
plt.savefig("ex2_thoughput_1024_sync.png", bbox_inches="tight")


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of threads")

ax.xaxis.set_ticks(np.arange(0, len(threads), 1))
ax.set_xticklabels(threads, rotation=45)
ax.set_xlim(-0.5, len(threads) - 0.5)
ax.set_ylabel("Throughput(Mops/sec)")

ax.plot(pthread_8192, label="pthread lock", color="red", marker='x')
ax.plot(tas_8192, label="tas lock", color="black", marker='x')
ax.plot(ttas_8192, label="ttas lock", color="green", marker='x')
ax.plot(array_8192, label="array lock", color="orange", marker='x')
ax.plot(clh_8192, label="clh lock", color="grey", marker='x')


plt.title("Throughput for size=8192")
lgd = plt.legend()

lgd.draw_frame(False)
plt.savefig("ex2_thoughput_8192_sync.png", bbox_inches="tight")
