%config InlineBackend.figure_format = 'retina'
%matplotlib inline
import matplotlib
import math

import matplotlib.cm as cm  # colormap
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
plt.rcParams["font.size"] = 20

plt.rcParams['font.family'] = 'Arial' #使用するフォント名
plt.rcParams["text.usetex"] =True
plt.rc('text', usetex=True)
# Axesを追加
#plt.figure(1)
fig = plt.figure(figsize=(20,8)) ##サイズ指定 (横の長さ,縦の長さ)

#1番目のグラフ
ax1 = fig.add_subplot(121) #位置を指定 今は縦に1個, 横に2個，このグラフは1番目 -> (121)と書く

plt.xscale('log')
plt.yscale('log')

#エラーバー付きのグラフの描き方
omega,gamma0,G1,G2,G0,sG1,sG2 = np.loadtxt("./pm0.9_SS/dp1e-5/omega1e-4/shear_dp0.00001_omega0.00010.dat",comments='!', unpack=True)
ax1.errorbar(gamma0,G1-G0,sG1-0.02*G0, ecolor="purple",marker="o",color="purple",capsize=5,linestyle="-",markersize=12,lw=3.5,label=r"$(\delta\varphi,\omega)=(10^{-5},10^{-4})$")

omega,gamma0,G1,G2,G0,sG1,sG2 = np.loadtxt("./pm0.9_SS/dp1e-5/omega1e-3/shear_dp0.00001_omega0.00100.dat",comments='!', unpack=True)
ax1.errorbar(gamma0,G1-G0,sG1-0.02*G0, ecolor="blue",marker="^",color="blue",capsize=5,linestyle="-",markersize=12,lw=3.5,label=r"$(10^{-5},10^{-3})$")

omega,gamma0,G1,G2,G0,sG1,sG2 = np.loadtxt("./pm0.9_SS/dp1e-5/omega1e-2/shear_dp0.00001_omega0.01000.dat",comments='!', unpack=True)
ax1.errorbar(gamma0,G1-G0,sG1-0.02*G0, ecolor="green",marker="s",color="green",capsize=5,linestyle="-",markersize=12,lw=3.5,label=r"$(10^{-5},10^{-2})$")

omega,gamma0,G1,G2,G0,sG1,sG2 = np.loadtxt("./pm0.9_SS/dp1e-4/omega1e-2/shear_dp0.00010_omega0.01000.dat",comments='!', unpack=True)
ax1.errorbar(gamma0,G1-G0,sG1-0.02*G0, ecolor="darkorange",marker="p",color="darkorange",capsize=5,linestyle="-",markersize=12,lw=3.5,label=r"$(10^{-4},10^{-2})$")

omega,gamma0,G1,G2,G0,sG1,sG2 = np.loadtxt("./pm0.9_SS/dp1e-3/omega1e-2/shear_dp0.00100_omega0.01000.dat",comments='!', unpack=True)
ax1.errorbar(gamma0,G1-G0,sG1-0.02*G0, ecolor="red",marker="H",color="red",capsize=5,linestyle="-",markersize=12,lw=3.5,label=r"$(10^{-3},10^{-2})$")

ax1.text(3.e-9,0.02, r"(a)",size=40)

plt.xticks(color='k', size=40)
plt.yticks(color='k', size=40)
plt.xlabel(r"$$\gamma$$",color='k', size=40)
plt.ylabel(r"$\Delta G'(\omega,\gamma)$",color='k', size=40)
#目盛設定
plt.xlim(1.e-7,1.e-2)
plt.ylim(2.e-4,3.e-2)
plt.tick_params(which='major',width = 2, length = 12.5, direction='in',pad=10)
plt.tick_params(which='minor',width = 2, length = 5, direction='in',pad=10)
ax1.spines['top'].set_linewidth(3)
ax1.spines['bottom'].set_linewidth(3)
ax1.spines['left'].set_linewidth(3)
ax1.spines['right'].set_linewidth(3)
leg = plt.legend(loc='lower center', bbox_to_anchor=(1.1,1.02), ncol=3, fontsize=35,edgecolor="black")
leg.get_frame().set_linewidth(3)

plt.subplots_adjust(wspace=0.3, hspace=0.0)


#2番目のグラフ
ax2 = fig.add_subplot(122) #位置を指定 今は縦に1個, 横に2個，このグラフは2番目 -> (122)と書く

plt.xscale('log')
plt.yscale('log')

omega,gamma0,G1,G2,G0,sG1,sG2 = np.loadtxt("./pm0.9_SS/dp1e-5/omega1e-4/shear_dp0.00001_omega0.00010.dat",comments='!', unpack=True)
ax2.errorbar(gamma0/1.e-5,(G1-G0)/omega**0.5,(sG1-0.02*G0)/omega**0.5, ecolor="purple",marker="o",color="purple",capsize=5,linestyle="-",markersize=12,lw=3.5,label=r"$\omega=10^{-4}$")

omega,gamma0,G1,G2,G0,sG1,sG2 = np.loadtxt("./pm0.9_SS/dp1e-5/omega1e-3/shear_dp0.00001_omega0.00100.dat",comments='!', unpack=True)
ax2.errorbar(gamma0/1.e-5,(G1-G0)/omega**0.5,(sG1-0.02*G0)/omega**0.5, ecolor="blue",marker="^",color="blue",capsize=5,linestyle="-",markersize=12,lw=3.5,label=r"$\omega=10^{-3}$")

omega,gamma0,G1,G2,G0,sG1,sG2 = np.loadtxt("./pm0.9_SS/dp1e-5/omega1e-2/shear_dp0.00001_omega0.01000.dat",comments='!', unpack=True)
ax2.errorbar(gamma0/1.e-5,(G1-G0)/omega**0.5,(sG1-0.02*G0)/omega**0.5, ecolor="green",marker="s",color="green",capsize=5,linestyle="-",markersize=12,lw=3.5,label=r"$\omega=10^{-2}$")

omega,gamma0,G1,G2,G0,sG1,sG2 = np.loadtxt("./pm0.9_SS/dp1e-4/omega1e-2/shear_dp0.00010_omega0.01000.dat",comments='!', unpack=True)
ax2.errorbar(gamma0/1.e-4,(G1-G0)/omega**0.5,(sG1-0.02*G0)/omega**0.5, ecolor="darkorange",marker="p",color="darkorange",capsize=5,linestyle="-",markersize=12,lw=3.5,label=r"$\delta\varphi=10^{-4}$")

omega,gamma0,G1,G2,G0,sG1,sG2 = np.loadtxt("./pm0.9_SS/dp1e-3/omega1e-2/shear_dp0.00100_omega0.01000.dat",comments='!', unpack=True)
ax2.errorbar(gamma0/1.e-3,(G1-G0)/omega**0.5,(sG1-0.02*G0)/omega**0.5, ecolor="red",marker="H",color="red",capsize=5,linestyle="-",markersize=12,lw=3.5,label=r"$\delta\varphi=10^{-3}$")


x = np.linspace(-0.5,1.,1000)
y = 1.e-1*(10.0**x)**(-0.5)
ax2.plot(10.0**x, y, ls = "--",color = "black",lw=3.5,zorder=2)

ax2.text(3.e-2,0.08, r"$\propto\gamma^{-1/2}$",size=40)

ax2.text(8.e-5,0.25, r"(b)",size=40)

plt.xticks(color='k', size=40)
plt.yticks(color='k', size=40)
plt.xlabel(r"$$\gamma/\delta\varphi$$",color='k', size=40)
plt.ylabel(r"$\Delta G'(\omega,\gamma)/\omega^{1/2}$",color='k', size=40)
ax2.yaxis.set_label_coords(-0.3, 0.5)
# 目盛設定
plt.xlim(1.e-2,1.e+3)
plt.ylim(2.e-2,3.e-1)
#y軸の目盛りをこちらで指定した値だけ表示する (logスケール)
ax2.yaxis.set_major_locator(LogLocator(base=10.0, subs=[1.0]))
minor_locator = LogLocator(base=10.0, subs=range(2, 10), numticks=100)
ax2.yaxis.set_minor_locator(minor_locator)
selected_ticks = [2e-2, 3e-2, 5e-2, 2e-1, 3e-1]
ax2.tick_params(which='minor', width=1, length=5)
for tick in selected_ticks:
    exponent = int(np.floor(np.log10(tick)))
    coeff = tick / 10**exponent
    # 整数ならそのまま、そうでなければ小数表示
    if abs(coeff - round(coeff)) < 1e-6:
        coeff = int(round(coeff))
    label = rf"${coeff} \times 10^{{{exponent}}}$"
    ax2.text(
        -0.27, tick, label,
        va='center', ha='left',
        transform=ax2.get_yaxis_transform(),
        fontsize=35
    )
plt.tick_params(which='major',width = 2, length = 12.5, direction='in',pad=10)
plt.tick_params(which='minor',width = 2, length = 5, direction='in',pad=10)
ax2.spines['top'].set_linewidth(3)
ax2.spines['bottom'].set_linewidth(3)
ax2.spines['left'].set_linewidth(3)
ax2.spines['right'].set_linewidth(3)


plt.subplots_adjust(wspace=0.45, hspace=0.0) #2つのグラフの間隔を調整する

plt.savefig('./pm0.9_SS/Fig1_Delta_G1_gamma0.pdf',bbox_inches="tight")

plt.show()
