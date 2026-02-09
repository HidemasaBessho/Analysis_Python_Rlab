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
fig = plt.figure(figsize=(12,8)) ##サイズ指定##

ax1 = fig.add_subplot(111)

plt.xscale('log') #対数プロット
# plt.yscale('log')

t,Fs0,Fs1 = np.loadtxt("./glass/T1.00/Fs_T1.00_rho0.80.dat",comments='!', unpack=True) #データの読み込み
ax1.plot(t,Fs0,"-o",color="red",markersize=8,lw=3.5,label=r"$T=1.0$",zorder=2)
#x軸: t, y軸: Fs0, markerと線の種類: "-o", 色: "red", マーカーサイズ: 12, 線の太さ: 3.5, 凡例名: "$T=1.0$", zorder: グラフを表示する上下関係

t,Fs0,Fs1 = np.loadtxt("./glass/T0.72/Fs_T0.72_rho0.80.dat",comments='!', unpack=True) #データの読み込み
ax1.plot(t,Fs0,"-^",color="darkorange",markersize=8,lw=3.5,label=r"$T=0.72$",zorder=3)

t,Fs0,Fs1 = np.loadtxt("./glass/T0.64/Fs_T0.64_rho0.80.dat",comments='!', unpack=True) #データの読み込み
ax1.plot(t,Fs0,"-s",color="green",markersize=8,lw=3.5,label=r"$T=0.64$",zorder=4)

t,Fs0,Fs1 = np.loadtxt("./glass/T0.56/Fs_T0.56_rho0.80.dat",comments='!', unpack=True) #データの読み込み
ax1.plot(t,Fs0,"-D",color="blue",markersize=8,lw=3.5,label=r"$T=0.56$",zorder=5)

ax1.axhline(y=np.exp(-1),lw=3,color="black",linestyle=":",zorder=1) #x軸に並行な線 (y軸に並行な線の場合にはaxvlineにする)

ax1.text(1.5e-2,0.41, r"$F_s(q,t)=1/e$",size=32,color="black") #グラフに文字を入れる

plt.xticks(color='k', size=35) #x軸の目盛りの色('k'=黒)とサイズ
plt.yticks(color='k', size=35) #y軸の目盛りの色('k'=黒)とサイズ
plt.xlabel(r"$$t$$",color='k', size=35) #x軸のラベル色('k'=黒)とサイズ
plt.ylabel(r"$F_s(q=2\pi,t)$",color='k', size=35) #y軸のラベル色('k'=黒)とサイズ
#目盛設定
plt.xlim(1.e-2,1.e+4) #x軸の範囲
plt.ylim(0,1) #y軸の範囲
plt.tick_params(axis='x', which='major',width = 1, length = 10, direction='in',pad=10) #x軸の主目盛り -> width: 目盛りの太さ, length: 目盛りの長さ, direction: 目盛りの方向 ('in'は内側に表示), pad: 軸と目盛りの距離
plt.tick_params(axis='x',which='minor',width = 1, length = 5, direction='in')
ax1.tick_params(axis='y', which='major', labelsize=35, width=1, length=10, direction='in',pad=10)
ax1.tick_params(axis='y', which='minor', labelsize=35, width=1, length=5, direction='in')
ax1.spines['top'].set_linewidth(2.5) #グラフを囲む線の太さ
ax1.spines['bottom'].set_linewidth(2.5)
ax1.spines['left'].set_linewidth(2.5)
ax1.spines['right'].set_linewidth(2.5)
leg = plt.legend(loc='lower center', bbox_to_anchor=(0.85,0.525), ncol=1, fontsize=32,edgecolor="black",handletextpad=0.2,handlelength=1) #凡例 -> bbox_to_anchorで位置を調整, ncol: 列の数, edgecolor: 凡例の枠線の色, handletextpad: 凡例のプロットとラベル間の距離, handlelength: 凡例のプロットの長さ
leg.get_frame().set_linewidth(2.5) #凡例中のプロット線の太さ

plt.savefig('./glass/Fs_rho0.80.pdf',bbox_inches="tight") #保存, 各自ディレクトリを変更する

plt.show()
