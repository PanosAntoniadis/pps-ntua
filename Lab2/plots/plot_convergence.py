import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib


labels = ['Jacobi', 'GaussSeiderlSOR', 'RedBlackSOR']

iter_jac = np.zeros((3, 3))
iter_gau = np.zeros((3, 3))
iter_rb = np.zeros((3, 3))

tcomp_jac = np.zeros((3, 3))
tcomp_gau = np.zeros((3, 3))
tcomp_rb = np.zeros((3, 3))

tconv_jac = np.zeros((3, 3))
tconv_gau = np.zeros((3, 3))
tconv_rb = np.zeros((3, 3))

ttotal_jac = np.zeros((3, 3))
ttotal_gau = np.zeros((3, 3))
ttotal_rb = np.zeros((3, 3))

for file in sys.argv[1:]:
    fp = open(file)
    file_parts = file.split('_')
    line = fp.readlines()
    sample = int(file_parts[3].split('.')[0])
    if file_parts[3].split('.')[1] == 'err':
        continue
    if file_parts[1] == '16' and file_parts[2] == '4':
        jac = line[0].split(" ")
        gauss = line[1].split(" ")
        redblack = line[2].split(" ")
        iter_jac[0, sample] = jac[10]
        iter_gau[0, sample] = gauss[10]
        iter_rb[0, sample] = redblack[10]
        tcomp_jac[0, sample] = jac[12]
        tcomp_gau[0, sample] = gauss[12]
        tcomp_rb[0, sample] = redblack[12]
        tconv_jac[0, sample] = jac[17]
        tconv_gau[0, sample] = gauss[17]
        tconv_rb[0, sample] = redblack[17]
        ttotal_jac[0, sample] = jac[14]
        ttotal_gau[0, sample] = gauss[14]
        ttotal_rb[0, sample] = redblack[14]
    if file_parts[1] == '4' and file_parts[2] == '16':
        jac = line[0].split(" ")
        gauss = line[1].split(" ")
        redblack = line[2].split(" ")
        iter_jac[1, sample] = jac[10]
        iter_gau[1, sample] = gauss[10]
        iter_rb[1, sample] = redblack[10]
        tcomp_jac[1, sample] = jac[12]
        tcomp_gau[1, sample] = gauss[12]
        tcomp_rb[1, sample] = redblack[12]
        tconv_jac[1, sample] = jac[17]
        tconv_gau[1, sample] = gauss[17]
        tconv_rb[1, sample] = redblack[17]
        ttotal_jac[1, sample] = jac[14]
        ttotal_gau[1, sample] = gauss[14]
        ttotal_rb[1, sample] = redblack[14]
    if file_parts[1] == '8' and file_parts[2] == '8':
        jac = line[0].split(" ")
        gauss = line[1].split(" ")
        redblack = line[2].split(" ")
        iter_jac[2, sample] = jac[10]
        iter_gau[2, sample] = gauss[10]
        iter_rb[2, sample] = redblack[10]
        tcomp_jac[2, sample] = jac[12]
        tcomp_gau[2, sample] = gauss[12]
        tcomp_rb[2, sample] = redblack[12]
        tconv_jac[2, sample] = jac[17]
        tconv_gau[2, sample] = gauss[17]
        tconv_rb[2, sample] = redblack[17]
        ttotal_jac[2, sample] = jac[14]
        ttotal_gau[2, sample] = gauss[14]
        ttotal_rb[2, sample] = redblack[14]

# print(iter_jac)
# print(iter_gau)
# print(iter_rb)

# print(tcomp_jac)
# print(tcomp_gau)
# print(tcomp_rb)

# print(ttotal_jac)
# print(ttotal_gau)
# print(ttotal_rb)

# print(tconv_jac)
# print(tconv_gau)
# print(tconv_rb)

iter_jac_m = np.mean(iter_jac, axis=1)
iter_gau_m = np.mean(iter_gau, axis=1)
iter_rb_m = np.mean(iter_rb, axis=1)

tcomp_jac_m = np.mean(tcomp_jac, axis=1)
tcomp_gau_m = np.mean(tcomp_gau, axis=1)
tcomp_rb_m = np.mean(tcomp_rb, axis=1)

tconv_jac_m = np.mean(tconv_jac, axis=1)
tconv_gau_m = np.mean(tconv_gau, axis=1)
tconv_rb_m = np.mean(tconv_rb, axis=1)

ttotal_jac_m = np.mean(ttotal_jac, axis=1)
ttotal_gau_m = np.mean(ttotal_gau, axis=1)
ttotal_rb_m = np.mean(ttotal_rb, axis=1)

print(iter_jac_m)
print(iter_gau_m)
print(iter_rb_m)

print(tcomp_jac_m)
print(tcomp_gau_m)
print(tcomp_rb_m)

print(ttotal_jac_m)
print(ttotal_gau_m)
print(ttotal_rb_m)

print(tconv_jac_m)
print(tconv_gau_m)
print(tconv_rb_m)

tcomm_jac_m = ttotal_jac_m - tconv_jac_m - tcomp_jac_m
tcomm_gau_m = ttotal_gau_m - tconv_gau_m - tcomp_gau_m
tcomm_rb_m = ttotal_rb_m - tconv_rb_m - tcomp_rb_m

print(tcomm_jac_m)
print(tcomm_gau_m)
print(tcomm_rb_m)

barWidth = 0.1
# Set position of bar on X axis
r = np.arange(3)
r1 = [x + barWidth for x in r]
r2 = [x + barWidth for x in r1]

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Grid Size")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['16x4', '4x16', '8x8'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")


plt.bar(r, tcomp_jac_m, width=barWidth, color='blue')
plt.bar(r, tconv_jac_m, bottom=tcomp_jac_m, width=barWidth, color='yellow')
plt.bar(r, tcomm_jac_m, bottom=tconv_jac_m +
        tcomp_jac_m, width=barWidth, color='green')

plt.title("Time of Jacobi in 1024x1024 grid")
lgd = plt.legend(['computation', 'convergence', 'communication'])
lgd.draw_frame(False)
plt.savefig("bar_conv_jac.png", bbox_inches="tight")


barWidth = 0.1
# Set position of bar on X axis
r = np.arange(3)
r1 = [x + barWidth for x in r]
r2 = [x + barWidth for x in r1]

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Grid Size")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['16x4', '4x16', '8x8'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")


plt.bar(r, tcomp_gau_m, width=barWidth, color='blue')
plt.bar(r, tconv_gau_m, bottom=tcomp_gau_m, width=barWidth, color='yellow')
plt.bar(r, tcomm_gau_m, bottom=tconv_gau_m +
        tcomp_gau_m, width=barWidth, color='green')

plt.title("Time of GaussSeidelSOR in 1024x1024 grid")
lgd = plt.legend(['computation', 'convergence', 'communication'])
lgd.draw_frame(False)
plt.savefig("bar_conv_gau.png", bbox_inches="tight")


barWidth = 0.1
# Set position of bar on X axis
r = np.arange(3)
r1 = [x + barWidth for x in r]
r2 = [x + barWidth for x in r1]

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("Grid Size")

ax.xaxis.set_ticks(np.arange(0, len(r), 1))
ax.set_xticklabels(['16x4', '4x16', '8x8'], rotation=45)
ax.set_xlim(-0.5, len(r) - 0.5)
ax.set_ylabel("Time (s)")


plt.bar(r, tcomp_rb_m, width=barWidth, color='blue')
plt.bar(r, tconv_rb_m, bottom=tcomp_rb_m, width=barWidth, color='yellow')
plt.bar(r, tcomm_rb_m, bottom=tconv_rb_m +
        tcomp_rb_m, width=barWidth, color='green')

plt.title("Time of RedBlackSOR in 1024x1024 grid")
lgd = plt.legend(['computation', 'convergence', 'communication'])
lgd.draw_frame(False)
plt.savefig("bar_rb_jac.png", bbox_inches="tight")
