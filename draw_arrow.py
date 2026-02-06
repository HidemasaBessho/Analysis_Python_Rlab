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
fig = plt.figure(figsize=(13,8)) ##サイズ指定##

ax1 = fig.add_subplot(111)

plt.xscale('log')
# plt.yscale('log')

#plt.scatter(1, 0.845798, c='k',label="all")

dp,gamma,Us,Ue,fs,fe,Gs,Ge=np.loadtxt("./pm0.9_SS/dp1e-4/relax_slope_dp0.00010_range.dat", comments='!', unpack=True)
ax1.errorbar(gamma,Us,Ue,ecolor="red",marker="o",markerfacecolor="red",color="red",capsize=7,linestyle="none",markersize=10,lw=3.5,zorder=8)
ax1.errorbar(gamma,fs,fe,ecolor="blue",marker="^",markerfacecolor="blue",color="blue",capsize=7,linestyle="none",markersize=10,lw=3.5,zorder=9)
ax1.errorbar(gamma,Gs,Ge,ecolor="green",marker="s",markerfacecolor="green",color="green",capsize=7,linestyle="none",markersize=10,lw=3.5,zorder=7)


ax1.axhline(y=0.5,lw=1,color="red",linestyle="-",alpha=0.7)
ax1.axhline(y=0.84,lw=3,color="red",linestyle=":",alpha=0.7)

ax1.axhline(y=0.75,lw=1,color="blue",linestyle="-",alpha=0.7)
ax1.axhline(y=0.92,lw=3,color="blue",linestyle=":",alpha=0.7)

ax1.text(1.1,0.49, r"$\beta_{E}=1/2$",size=30,color="red")
ax1.text(1.1,0.83, r"$\beta_{E}=0.84$",size=30,color="red")

ax1.text(1.1,0.74, r"$\beta_{E}=3/4$",size=30,color="blue")
ax1.text(1.1,0.91, r"$\beta_{E}=0.92$",size=30,color="blue")


ax1.text(1.3e-05,1.065, r"$\gamma_{\mathrm{s}}(10^{-4})$",size=30,color="darkorange")
ax1.text(0.015,1.065, r"$\gamma_{\mathrm{y}}$",size=30,color="darkorange")


####矢印の描き方#####
#plt.annotate("",xy=(終点のx, 終点のy), xytext=(始点のx, 始点のy),arrowprops=dict(edgecolor=矢印の枠線の色,facecolor=矢印の塗りつぶしの色, shrink=0.05,linewidth=線の太さ))

plt.annotate("",xy=(1.66936679363601e-05, 1.0), xytext=(1.66936679363601e-05, 1.05),arrowprops=dict(edgecolor='darkorange',facecolor='none', shrink=0.05,linewidth=0.5))
plt.annotate("",xy=(0.0195954512783951, 1.0), xytext=(0.0195954512783951, 1.05),arrowprops=dict(edgecolor='darkorange',facecolor='darkorange', shrink=0.05,linewidth=0.5))


plt.xticks(color='k', size=35)
plt.yticks(color='k', size=35)
plt.xlabel(r"$$\gamma$$",color='k', size=35)
plt.ylabel(r"$\beta$",color='k', size=35)
#目盛設定
plt.xlim(9.e-8,1)
plt.ylim(0.3,1)
plt.tick_params(axis='x', which='major',width = 1, length = 10, direction='in',pad=12)
plt.tick_params(axis='x',which='minor',width = 1, length = 5, direction='in')
ax1.tick_params(axis='y', which='major', labelsize=35, width=1, length=10, direction='in',pad=12)
ax1.tick_params(axis='y', which='minor', labelsize=35, width=1, length=5, direction='in')
ax1.xaxis.set_ticks_position('both')
ax1.tick_params(axis='x', which='both', top=True)
ax1.spines['top'].set_linewidth(2.5)
ax1.spines['bottom'].set_linewidth(2.5)
ax1.spines['left'].set_linewidth(2.5)
ax1.spines['right'].set_linewidth(2.5)
leg=plt.legend(ncol=3, loc=2, borderaxespad=0.35, fontsize=27,frameon=True,edgecolor="black",handletextpad=0.2,handlelength=1)
leg.get_frame().set_linewidth(2.5)


plt.savefig('./pm0.9_SS/dp1e-4/Fig_relax_slope.pdf',bbox_inches="tight")
plt.show()
