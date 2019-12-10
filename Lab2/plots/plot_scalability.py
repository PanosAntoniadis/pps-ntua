import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
import math
x = ['1', '2', '4', '8', '16', '32', '64']

t_jac_2048 = np.zeros((7, 3))
t_jac_4096 = np.zeros((7, 3))
t_jac_6144 = np.zeros((7, 3))

t_gau_2048 = np.zeros((7, 3))
t_gau_4096 = np.zeros((7, 3))
t_gau_6144 = np.zeros((7, 3))

t_rb_2048 = np.zeros((7, 3))
t_rb_4096 = np.zeros((7, 3))
t_rb_6144 = np.zeros((7, 3))

for file in sys.argv[1:]:
    fp = open(file)
    file_parts = file.split('_')
    line = fp.readlines()[0]
    sample = int(file_parts[3])
    method = file_parts[0].split('/')[-1]
    if method == 'jacobi':
        if file_parts[1][1:] == '2048':
            core = int(file_parts[2][1:])
            t_jac_2048[int(math.log(core, 2)), sample] = line.split(' ')[14]
        if file_parts[1][1:] == '4096':
            core = int(file_parts[2][1:])
            t_jac_4096[int(math.log(core, 2)), sample] = line.split(' ')[14]
        if file_parts[1][1:] == '6144':
            core = int(file_parts[2][1:])
            t_jac_6144[int(math.log(core, 2)), sample] = line.split(' ')[14]
    if method == 'seidelsor':
        if file_parts[1][1:] == '2048':
            core = int(file_parts[2][1:])
            t_gau_2048[int(math.log(core, 2)), sample] = line.split(' ')[14]
        if file_parts[1][1:] == '4096':
            core = int(file_parts[2][1:])
            t_gau_4096[int(math.log(core, 2)), sample] = line.split(' ')[14]
        if file_parts[1][1:] == '6144':
            core = int(file_parts[2][1:])
            t_gau_6144[int(math.log(core, 2)), sample] = line.split(' ')[14]
    if method == 'redblacksor':
        if file_parts[1][1:] == '2048':
            core = int(file_parts[2][1:])
            t_rb_2048[int(math.log(core, 2)), sample] = line.split(' ')[14]
        if file_parts[1][1:] == '4096':
            core = int(file_parts[2][1:])
            t_rb_4096[int(math.log(core, 2)), sample] = line.split(' ')[14]
        if file_parts[1][1:] == '6144':
            core = int(file_parts[2][1:])
            t_rb_6144[int(math.log(core, 2)), sample] = line.split(' ')[14]


t_jac_2048_m = np.mean(t_jac_2048, axis=1)
t_jac_4096_m = np.mean(t_jac_4096, axis=1)
t_jac_6144_m = np.mean(t_jac_6144, axis=1)

t_gau_2048_m = np.mean(t_gau_2048, axis=1)
t_gau_4096_m = np.mean(t_gau_4096, axis=1)
t_gau_6144_m = np.mean(t_gau_6144, axis=1)

t_rb_2048_m = np.mean(t_rb_2048, axis=1)
t_rb_4096_m = np.mean(t_rb_4096, axis=1)
t_rb_6144_m = np.mean(t_rb_6144, axis=1)


'''
print(t_jac_2048_m)
print(t_jac_4096_m)
print(t_jac_6144_m)

print(t_gau_2048_m)
print(t_gau_4096_m)
print(t_gau_6144_m)

print(t_rb_2048_m)
print(t_rb_4096_m)
print(t_rb_6144_m)

'''

s_jac_2048_m = t_jac_2048_m[0] / t_jac_2048_m
s_jac_4096_m = t_jac_4096_m[0] / t_jac_4096_m
s_jac_6144_m = t_jac_6144_m[0] / t_jac_6144_m

s_gau_2048_m = t_gau_2048_m[0] / t_gau_2048_m
s_gau_4096_m = t_gau_4096_m[0] / t_gau_4096_m
s_gau_6144_m = t_gau_6144_m[0] / t_gau_6144_m

s_rb_2048_m = t_rb_2048_m[0] / t_rb_2048_m
s_rb_4096_m = t_rb_4096_m[0] / t_rb_4096_m
s_rb_6144_m = t_rb_6144_m[0] / t_rb_6144_m


fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of MPI processes")

ax.xaxis.set_ticks(np.arange(0, len(x), 1))
ax.set_xticklabels(x, rotation=45)
ax.set_xlim(-0.5, len(x) - 0.5)
ax.set_ylabel("Speedup")

ax.plot(s_jac_2048_m, label="jacobian", color="blue", marker='x')
ax.plot(s_gau_2048_m, label="seidelsor", color="red", marker='x')
ax.plot(s_rb_2048_m, label="redblacksor", color="black", marker='x')


plt.title("Speedup in 2048x2048 table")
lgd = plt.legend()
lgd.draw_frame(False)
plt.savefig("speedup_2048.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of MPI processes")

ax.xaxis.set_ticks(np.arange(0, len(x), 1))
ax.set_xticklabels(x, rotation=45)
ax.set_xlim(-0.5, len(x) - 0.5)
ax.set_ylabel("Speedup")

ax.plot(s_jac_4096_m, label="jacobian", color="blue", marker='x')
ax.plot(s_gau_4096_m, label="seidelsor", color="red", marker='x')
ax.plot(s_rb_4096_m, label="redblacksor", color="black", marker='x')


plt.title("Speedup in 4096x4096 table")
lgd = plt.legend()
lgd.draw_frame(False)
plt.savefig("speedup_4096.png", bbox_inches="tight")

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of MPI processes")

ax.xaxis.set_ticks(np.arange(0, len(x), 1))
ax.set_xticklabels(x, rotation=45)
ax.set_xlim(-0.5, len(x) - 0.5)
ax.set_ylabel("Speedup")

ax.plot(s_jac_6144_m, label="jacobian", color="blue", marker='x')
ax.plot(s_gau_6144_m, label="seidelsor", color="red", marker='x')
ax.plot(s_rb_6144_m, label="redblacksor", color="black", marker='x')


plt.title("Speedup in 6144x6144 table")
lgd = plt.legend()
lgd.draw_frame(False)
plt.savefig("speedup_6144.png", bbox_inches="tight")
