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
fig = plt.figure(figsize=(8,8)) ##サイズ指定##

ax1 = fig.add_subplot(111)

plt.xscale('log')
plt.yscale('log')

omega,gamma0,G1,G2,G0,sG1,sG2 = np.loadtxt("./pm0.9_SS/dp1e-4/omega1e-2/shear_dp0.00010_omega0.01000.dat",comments='!', unpack=True) #データの読み込み
ax1.plot(gamma0,(G1-G0)/(G1[0]-G0[0]), marker="o",color="red",linestyle="-",markersize=12,lw=3.5,label=r"$\Delta G'_{\mathrm{Sim}}(\gamma)$",zorder=5)
#x軸: gamma0, y軸: (G1-G0)/(G1[0]-G0[0]), markerの種類: "o", 色: "red", 線種: "-", マーカーサイズ: 12, 線の太さ: 3.5, 凡例名: "$\Delta G'_{\mathrm{Sim}}(\gamma)$", zorder: グラフを表示する上下関係

gamma,txy0,txyinf,P0,Pinf,E0,Einf,Einit,z0,zinf,drinf = np.loadtxt("/Users/besshohidemasa/Rlab/stress_relaxation/pm0.9_SS/dp1e-4/stress_affine_AQS_dp0.00010.dat",comments='!', unpack=True)
ax1.plot(gamma,(txyinf/gamma)/(txyinf[0]/gamma[0]),"-^",color="darkgray",markerfacecolor="darkgray",markeredgecolor="darkgray",markersize=12,lw=3.5,markeredgewidth=1.5,label=r"$G_{\mathrm{qs}}(\gamma)$",zorder=4)

omega,gamma0,G1,G2,G0 = np.loadtxt("./pm0.9_SS/dp1e-4/omega1e-2/Gomega_dp1em4_omega1em2.dat",comments='!', unpack=True)
ax1.plot(gamma0,(G1-G0)/(G1[0]-G0[0]),"o",color="red",markerfacecolor="none",markeredgecolor="red",markersize=12,lw=3.5,markeredgewidth=2,label=r"$\Delta G'_{\mathrm{FT}}(\gamma)$",zorder=3)

gamma0,txy0,txye0,P0,E0,f0,z0,xi0=np.loadtxt("/Users/besshohidemasa/Rlab/stress_relaxation/pm0.9_SS/dp1e-4/Affine_stress_dp0.00010.dat", comments='!', unpack=True,skiprows=1)
ax1.plot(gamma0,(txy0/gamma0)/(txy0[0]/gamma0[0]),"-",markersize=12,linewidth=3.5,color="darkgray",label=r"$G(t=0,\gamma)$",markeredgewidth=1.5,zorder=2)

ax1.axvline(x=1.66936679363601e-05,lw=1.5,color="darkgray",linestyle=":",zorder=1)　#y軸に並行な線

ax1.text(7.e-6,0.11, r"$\gamma_{\mathrm{s}}$",size=35,color="black") #グラフに文字を入れる

plt.xticks(color='k', size=35) #x軸の目盛りの色('k'=黒)とサイズ
plt.yticks(color='k', size=35) #y軸の目盛りの色('k'=黒)とサイズ
plt.xlabel(r"$$\gamma$$",color='k', size=35) #x軸のラベル色('k'=黒)とサイズ
plt.ylabel(r"$G(\gamma)/G(\gamma=0)$",color='k', size=35)　#y軸のラベル色('k'=黒)とサイズ
#目盛設定
plt.xlim(1.e-6,1.e-1) #x軸の範囲
plt.ylim(1.e-1,1.2) #y軸の範囲
ax1.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10)*0.1, numticks=10)) #y軸は今の設定だと範囲が狭いので，強制的に目盛りを表示させる
plt.tick_params(axis='x', which='major',width = 1, length = 10, direction='in',pad=10) #x軸の主目盛り -> width: 目盛りの太さ, length: 目盛りの長さ, direction: 目盛りの方向 ('in'は内側に表示), pad: 軸と目盛りの距離
plt.tick_params(axis='x',which='minor',width = 1, length = 5, direction='in')
ax1.tick_params(axis='y', which='major', labelsize=35, width=1, length=10, direction='in',pad=10)
ax1.tick_params(axis='y', which='minor', labelsize=35, width=1, length=5, direction='in')
ax1.spines['top'].set_linewidth(2.5) #グラフを囲む線の太さ
ax1.spines['bottom'].set_linewidth(2.5)
ax1.spines['left'].set_linewidth(2.5)
ax1.spines['right'].set_linewidth(2.5)
leg = plt.legend(loc='lower center', bbox_to_anchor=(1.25,0.3), ncol=1, fontsize=30,edgecolor="black",handletextpad=0.2,handlelength=1) #凡例 -> bbox_to_anchorで位置を調整, ncol: 列の数, edgecolor: 凡例の枠線の色, handletextpad: 凡例のプロットとラベル間の距離, handlelength: 凡例のプロットの長さ
leg.get_frame().set_linewidth(2.5) #凡例中のプロット線の太さ

plt.savefig('./pm0.9_SS/dp1e-4/omega1e-2/Fig6_FT_G_gamma0_dp1em4_omega1em2.pdf',bbox_inches="tight") #保存, 各自ディレクトリを変更する

plt.show()
