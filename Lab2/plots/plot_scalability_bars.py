import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
import math
x = ['8', '16', '32', '64']

t_jac_2048 = np.zeros((4, 3))
t_jac_4096 = np.zeros((4, 3))
t_jac_6144 = np.zeros((4, 3))
t_gau_2048 = np.zeros((4, 3))
t_gau_4096 = np.zeros((4, 3))
t_gau_6144 = np.zeros((4, 3))
t_rb_2048 = np.zeros((4, 3))
t_rb_4096 = np.zeros((4, 3))
t_rb_6144 = np.zeros((4, 3))

tcomp_jac_2048 = np.zeros((4, 3))
tcomp_jac_4096 = np.zeros((4, 3))
tcomp_jac_6144 = np.zeros((4, 3))
tcomp_gau_2048 = np.zeros((4, 3))
tcomp_gau_4096 = np.zeros((4, 3))
tcomp_gau_6144 = np.zeros((4, 3))
tcomp_rb_2048 = np.zeros((4, 3))
tcomp_rb_4096 = np.zeros((4, 3))
tcomp_rb_6144 = np.zeros((4, 3))

for file in sys.argv[1:]:
    fp = open(file)
    file_parts = file.split('_')
    print(file)
    line = fp.readlines()[0]
    sample = int(file_parts[3])
    method = file_parts[0].split('/')[-1]
    if method == 'jacobi':
        if file_parts[1][1:] == '2048':
            core = int(file_parts[2][1:])
            t_jac_2048[int(math.log(core, 2)) - 3,
                       sample] = line.split(' ')[14]
            tcomp_jac_2048[int(math.log(core, 2)) - 3,
                           sample] = line.split(' ')[12]
        if file_parts[1][1:] == '4096':
            core = int(file_parts[2][1:])
            t_jac_4096[int(math.log(core, 2)) - 3,
                       sample] = line.split(' ')[14]
            tcomp_jac_4096[int(math.log(core, 2)) - 3,
                           sample] = line.split(' ')[12]
        if file_parts[1][1:] == '6144':
            core = int(file_parts[2][1:])
            t_jac_6144[int(math.log(core, 2)) - 3,
                       sample] = line.split(' ')[14]
            tcomp_jac_6144[int(math.log(core, 2)) - 3,
                           sample] = line.split(' ')[12]
    if method == 'seidelsor':
        if file_parts[1][1:] == '2048':
            core = int(file_parts[2][1:])
            t_gau_2048[int(math.log(core, 2)) - 3,
                       sample] = line.split(' ')[14]
            tcomp_gau_2048[int(math.log(core, 2)) - 3,
                           sample] = line.split(' ')[12]
        if file_parts[1][1:] == '4096':
            core = int(file_parts[2][1:])
            t_gau_4096[int(math.log(core, 2)) - 3,
                       sample] = line.split(' ')[14]
            tcomp_gau_4096[int(math.log(core, 2)) - 3,
                           sample] = line.split(' ')[12]
        if file_parts[1][1:] == '6144':
            core = int(file_parts[2][1:])
            t_gau_6144[int(math.log(core, 2)) - 3,
                       sample] = line.split(' ')[14]
            tcomp_gau_6144[int(math.log(core, 2)) - 3,
                           sample] = line.split(' ')[12]
    if method == 'redblacksor':
        if file_parts[1][1:] == '2048':
            core = int(file_parts[2][1:])
            t_rb_2048[int(math.log(core, 2)) - 3, sample] = line.split(' ')[14]
            tcomp_rb_2048[int(math.log(core, 2)) - 3,
                          sample] = line.split(' ')[12]
        if file_parts[1][1:] == '4096':
            core = int(file_parts[2][1:])
            t_rb_4096[int(math.log(core, 2)) - 3, sample] = line.split(' ')[14]
            tcomp_rb_4096[int(math.log(core, 2)) - 3,
                          sample] = line.split(' ')[12]
        if file_parts[1][1:] == '6144':
            core = int(file_parts[2][1:])
            t_rb_6144[int(math.log(core, 2)) - 3, sample] = line.split(' ')[14]
            tcomp_rb_6144[int(math.log(core, 2)) - 3,
                          sample] = line.split(' ')[12]

t_jac_2048_m = np.mean(t_jac_2048, axis=1)
t_jac_4096_m = np.mean(t_jac_4096, axis=1)
t_jac_6144_m = np.mean(t_jac_6144, axis=1)
t_gau_2048_m = np.mean(t_gau_2048, axis=1)
t_gau_4096_m = np.mean(t_gau_4096, axis=1)
t_gau_6144_m = np.mean(t_gau_6144, axis=1)
t_rb_2048_m = np.mean(t_rb_2048, axis=1)
t_rb_4096_m = np.mean(t_rb_4096, axis=1)
t_rb_6144_m = np.mean(t_rb_6144, axis=1)

tcomp_jac_2048_m = np.mean(tcomp_jac_2048, axis=1)
tcomp_jac_4096_m = np.mean(tcomp_jac_4096, axis=1)
tcomp_jac_6144_m = np.mean(tcomp_jac_6144, axis=1)
tcomp_gau_2048_m = np.mean(tcomp_gau_2048, axis=1)
tcomp_gau_4096_m = np.mean(tcomp_gau_4096, axis=1)
tcomp_gau_6144_m = np.mean(tcomp_gau_6144, axis=1)
tcomp_rb_2048_m = np.mean(tcomp_rb_2048, axis=1)
tcomp_rb_4096_m = np.mean(tcomp_rb_4096, axis=1)
tcomp_rb_6144_m = np.mean(tcomp_rb_6144, axis=1)

print([t_jac_2048_m[0], t_gau_2048_m[0], t_rb_2048_m[0]])
print([tcomp_jac_2048_m[0], tcomp_gau_2048_m[0],
       tcomp_rb_2048_m[0]])
barWidth = 0.1
# Set position of bar on X axis
r = np.arange(3)

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['Jacobi', 'GaussSeidelSOR', 'RedBlackSOR'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")

plt.bar(r, [t_jac_2048_m[0], t_gau_2048_m[0], t_rb_2048_m[0]],
        width=barWidth, color='blue')
plt.bar(r, [tcomp_jac_2048_m[0], tcomp_gau_2048_m[0],
            tcomp_rb_2048_m[0]], width=barWidth, color='green')

plt.title("Time in 2048x2048 grid using 8 processes")
lgd = plt.legend(['total (includes green part)', 'computation'])
lgd.draw_frame(False)
plt.savefig("bar_c8_2048.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['Jacobi', 'GaussSeidelSOR', 'RedBlackSOR'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")

plt.bar(r, [t_jac_2048_m[1], t_gau_2048_m[1], t_rb_2048_m[1]],
        width=barWidth, color='blue')
plt.bar(r, [tcomp_jac_2048_m[1], tcomp_gau_2048_m[1],
            tcomp_rb_2048_m[1]], width=barWidth, color='green')

plt.title("Time in 2048x2048 grid using 16 processes")
lgd = plt.legend(['total (includes green part)', 'computation'])
lgd.draw_frame(False)
plt.savefig("bar_c16_2048.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['Jacobi', 'GaussSeidelSOR', 'RedBlackSOR'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")

plt.bar(r, [t_jac_2048_m[2], t_gau_2048_m[2], t_rb_2048_m[2]],
        width=barWidth, color='blue')
plt.bar(r, [tcomp_jac_2048_m[2], tcomp_gau_2048_m[2],
            tcomp_rb_2048_m[2]], width=barWidth, color='green')

plt.title("Time in 2048x2048 grid using 32 processes")
lgd = plt.legend(['total (includes green part)', 'computation'])
lgd.draw_frame(False)
plt.savefig("bar_c32_2048.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['Jacobi', 'GaussSeidelSOR', 'RedBlackSOR'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")

plt.bar(r, [t_jac_2048_m[3], t_gau_2048_m[3], t_rb_2048_m[3]],
        width=barWidth, color='blue')
plt.bar(r, [tcomp_jac_2048_m[3], tcomp_gau_2048_m[3],
            tcomp_rb_2048_m[3]], width=barWidth, color='green')

plt.title("Time in 2048x2048 grid using 64 processes")
lgd = plt.legend(['total (includes green part)', 'computation'])
lgd.draw_frame(False)
plt.savefig("bar_c64_2048.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['Jacobi', 'GaussSeidelSOR', 'RedBlackSOR'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")

plt.bar(r, [t_jac_4096_m[0], t_gau_4096_m[0], t_rb_4096_m[0]],
        width=barWidth, color='blue')
plt.bar(r, [tcomp_jac_4096_m[0], tcomp_gau_4096_m[0],
            tcomp_rb_4096_m[0]], width=barWidth, color='green')

plt.title("Time in 4096x4096 grid using 8 processes")
lgd = plt.legend(['total (includes green part)', 'computation'])
lgd.draw_frame(False)
plt.savefig("bar_c8_4096.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['Jacobi', 'GaussSeidelSOR', 'RedBlackSOR'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")

plt.bar(r, [t_jac_4096_m[1], t_gau_4096_m[1], t_rb_4096_m[1]],
        width=barWidth, color='blue')
plt.bar(r, [tcomp_jac_4096_m[1], tcomp_gau_4096_m[1],
            tcomp_rb_4096_m[1]], width=barWidth, color='green')

plt.title("Time in 4096x4096 grid using 16 processes")
lgd = plt.legend(['total (includes green part)', 'computation'])
lgd.draw_frame(False)
plt.savefig("bar_c16_4096.png", bbox_inches="tight")


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['Jacobi', 'GaussSeidelSOR', 'RedBlackSOR'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")

plt.bar(r, [t_jac_4096_m[2], t_gau_4096_m[2], t_rb_4096_m[2]],
        width=barWidth, color='blue')
plt.bar(r, [tcomp_jac_4096_m[2], tcomp_gau_4096_m[2],
            tcomp_rb_4096_m[2]], width=barWidth, color='green')

plt.title("Time in 4096x4096 grid using 32 processes")
lgd = plt.legend(['total (includes green part)', 'computation'])
lgd.draw_frame(False)
plt.savefig("bar_c32_4096.png", bbox_inches="tight")


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['Jacobi', 'GaussSeidelSOR', 'RedBlackSOR'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")

plt.bar(r, [t_jac_4096_m[3], t_gau_4096_m[3], t_rb_4096_m[3]],
        width=barWidth, color='blue')
plt.bar(r, [tcomp_jac_4096_m[3], tcomp_gau_4096_m[3],
            tcomp_rb_4096_m[3]], width=barWidth, color='green')

plt.title("Time in 4096x4096 grid using 64 processes")
lgd = plt.legend(['total (includes green part)', 'computation'])
lgd.draw_frame(False)
plt.savefig("bar_c64_4096.png", bbox_inches="tight")


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['Jacobi', 'GaussSeidelSOR', 'RedBlackSOR'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")

plt.bar(r, [t_jac_6144_m[0], t_gau_6144_m[0], t_rb_6144_m[0]],
        width=barWidth, color='blue')
plt.bar(r, [tcomp_jac_6144_m[0], tcomp_gau_6144_m[0],
            tcomp_rb_6144_m[0]], width=barWidth, color='green')

plt.title("Time in 6144x6144 grid using 8 processes")
lgd = plt.legend(['total (includes green part)', 'computation'])
lgd.draw_frame(False)
plt.savefig("bar_c8_6144.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['Jacobi', 'GaussSeidelSOR', 'RedBlackSOR'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")

plt.bar(r, [t_jac_6144_m[1], t_gau_6144_m[1], t_rb_6144_m[1]],
        width=barWidth, color='blue')
plt.bar(r, [tcomp_jac_6144_m[1], tcomp_gau_6144_m[1],
            tcomp_rb_6144_m[1]], width=barWidth, color='green')

plt.title("Time in 6144x6144 grid using 16 processes")
lgd = plt.legend(['total (includes green part)', 'computation'])
lgd.draw_frame(False)
plt.savefig("bar_c16_6144.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['Jacobi', 'GaussSeidelSOR', 'RedBlackSOR'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")

plt.bar(r, [t_jac_6144_m[2], t_gau_6144_m[2], t_rb_6144_m[2]],
        width=barWidth, color='blue')
plt.bar(r, [tcomp_jac_6144_m[2], tcomp_gau_6144_m[2],
            tcomp_rb_6144_m[2]], width=barWidth, color='green')

plt.title("Time in 6144x6144 grid using 32 processes")
lgd = plt.legend(['total (includes green part)', 'computation'])
lgd.draw_frame(False)
plt.savefig("bar_c32_6144.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Method")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['Jacobi', 'GaussSeidelSOR', 'RedBlackSOR'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")

plt.bar(r, [t_jac_6144_m[3], t_gau_6144_m[3], t_rb_6144_m[3]],
        width=barWidth, color='blue')
plt.bar(r, [tcomp_jac_6144_m[3], tcomp_gau_6144_m[3],
            tcomp_rb_6144_m[3]], width=barWidth, color='green')

plt.title("Time in 6144x6144 grid using 64 processes")
lgd = plt.legend(['total (includes green part)', 'computation'])
lgd.draw_frame(False)
plt.savefig("bar_c64_6144.png", bbox_inches="tight")
