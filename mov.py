import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection, LineCollection
from matplotlib.colors import LogNorm
from matplotlib.patches import Circle
import matplotlib.animation as animation

# -----------------------
# Matplotlib settings
# -----------------------
plt.rcParams['font.family'] = 'Arial'
plt.rcParams["text.usetex"] = True
plt.rcParams["font.size"] = 25

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)

ax.set_aspect('equal')
for spine in ax.spines.values():
    spine.set_linewidth(3)

ax.tick_params(which='major', width=2, length=10)
ax.tick_params(axis='x', labelsize=40)
ax.tick_params(axis='y', labelsize=40)

ims = []

# -----------------------
# System parameters
# -----------------------
Np  = 1156
phi = 0.8449989999999936 - 5.e-3
L   = np.sqrt(math.pi * Np * (1.0 + 1.4**2) / 8.0 / phi)
V   = L * L

ax.set_xlim(0, L + 0.02686637712035236 * L)
ax.set_ylim(0, L)
ax.set_xticks([0, 10, 20, 30, 40])
ax.set_yticks([0, 10, 20, 30, 40])

# -----------------------
# Load strain data
# -----------------------
cnt, t, gamma_all, gamma_observe = np.loadtxt("./gamma_time_0.dat", comments='#', unpack=True)

# ======================================================
# Colorbar (作成は1回だけ)
# ======================================================
dummy_lc = LineCollection([], cmap="Reds",norm=LogNorm(vmin=1e-16, vmax=1e-8))
ax.add_collection(dummy_lc)

cbar = fig.colorbar(dummy_lc, ax=ax)
cbar.set_label(r"$|\sigma_{xy}^{jk}|$", size=40)
cbar.ax.tick_params(labelsize=40)

# ======================================================
# Animation frames
# ======================================================
for step in range(0, 62831):

    if step % 300 != 0:
        continue #300ステップに一回図示する

    x, y, a = np.loadtxt("./coord_cnt{:d}_0.dat".format(step),comments='#', unpack=True)
    gamma = gamma_all[step]

    contacts = []
    stress_list = []

    # -------------------------------
    # Contact + stress calculation
    # -------------------------------
    for i in range(Np):
        for j in range(i+1, Np):

            dx = x[i] - x[j]
            dy = y[i] - y[j]
            dy_temp = dy

            # Lees–Edwards BC
            dy -= L * math.floor((dy + 0.5*L) / L)
            dx -= gamma * L * math.floor((dy_temp + 0.5*L) / L)
            dx -= L * math.floor((dx + 0.5*L) / L)

            dr  = math.sqrt(dx*dx + dy*dy)
            aij = 0.5 * (a[i] + a[j])

            if dr < aij:
                fij = (1.0 - dr/aij) / aij
                sij = (fij * dx * dy) / (dr * V)

                stress_list.append(abs(sij))
                contacts.append((x[i], y[i], dx, dy, sij))

    stress_list = np.array(stress_list)
    s_mean = np.mean(stress_list)

    # -------------------------------
    # Build line segments
    # -------------------------------
    lines = []
    linewidths = []
    colors = []

    for xi, yi, dx, dy, sij in contacts:

        xj = xi - dx
        yj = yi - dy
        val = abs(sij)

        if yj < 0 or yj > L:
            yb = 0 if yj < 0 else L
            t  = (yb - yi) / (yj - yi)
            xb = xi + t * (xj - xi)

            lines.append([(xi, yi), (xb, yb)])

            yj2 = yj + L if yj < 0 else yj - L
            yi2 = yi + L if yj < 0 else yi - L
            lines.append([(xi, yi2), (xj, yj2)])
        else:
            lines.append([(xi, yi), (xj, yj)])

        linewidths.append(1.5 + 0.1 * val / s_mean)
        colors.append(val)

    # -------------------------------
    # Particles
    # -------------------------------
    patches = [mpatches.Circle((x[i], y[i]), radius=0.5*a[i]) for i in range(Np)] #list内包表記
    pc = PatchCollection(patches, facecolor="lightgray",edgecolor="none", alpha=0.8)
    ax.add_collection(pc)

    # -------------------------------
    # Stress chains
    # -------------------------------
    lc = LineCollection(lines,cmap="Reds",linewidths=linewidths,norm=LogNorm(vmin=1e-16, vmax=1e-8),alpha=0.9)
    lc.set_array(np.array(colors))
    ax.add_collection(lc)

    ims.append([pc, lc])

# -----------------------
# Save animation
# -----------------------
ani = animation.ArtistAnimation(fig, ims, interval=100)
ani.save("./stress_chain.gif", writer="imagemagick")
