%config InlineBackend.figure_format = 'retina'
%matplotlib inline
import matplotlib
import math

import matplotlib.cm as cm  # colormap
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.size"] = 20

plt.rcParams['font.family'] = 'Arial' #使用するフォント名
plt.rcParams["text.usetex"] =True
plt.rc('text', usetex=True)

fig = plt.figure(figsize=(12,8)) ##サイズ指定##
ax1 = fig.add_subplot(111)

plt.xscale('log')
plt.yscale('log')

gamma,txy,P,U,xi,dr,dr0,z=np.loadtxt("./dp1e-5/AQS/pm0.9/Shear_dp0.000010.dat", comments='!', unpack=True, skiprows=1)
ax1.plot(gamma/1.e-5,txy/P/(1.e-5)**0.5,"-o",markersize=6,linewidth=3.0,color="purple",label=r"$\delta\varphi=10^{-5}$")

gamma,txy,P,U,xi,dr,dr0,z=np.loadtxt("./dp1e-4/AQS/pm0.9/Shear_dp0.000100.dat", comments='!', unpack=True, skiprows=1)
ax1.plot(gamma/1.e-4,txy/P/(1.e-4)**0.5,"-^",markersize=6,linewidth=3.0,color="blue",label=r"$10^{-4}$")

gamma,txy,P,U,xi,dr,dr0,z=np.loadtxt("./dp5e-4/Shear_dp0.000500.dat", comments='!', unpack=True, skiprows=1)
ax1.plot(gamma/5.e-4,txy/P/(5.e-4)**0.5,"-s",markersize=6,linewidth=3.0,color="deepskyblue",label=r"$5\times10^{-4}$")

gamma,txy,P,U,xi,dr,dr0,z=np.loadtxt("./dp1e-3/AQS/pm0.9/Shear_dp0.001000.dat", comments='!', unpack=True, skiprows=1)
ax1.plot(gamma/1.e-3,txy/P/(1.e-3)**0.5,"-D",markersize=6,linewidth=3.0,color="green",label=r"$10^{-3}$")

gamma,txy,P,U,xi,dr,dr0,z=np.loadtxt("./dp3e-3/Shear_dp0.003000.dat", comments='!', unpack=True, skiprows=1)
ax1.plot(gamma/3.e-3,txy/P/(3.e-3)**0.5,"-p",markersize=6,linewidth=3.0,color="darkorange",label=r"$3\times10^{-3}$")

gamma,txy,P,U,xi,dr,dr0,z=np.loadtxt("./dp1e-2/Shear_dp0.010000.dat", comments='!', unpack=True, skiprows=1)
ax1.plot(gamma/1.e-2,txy/P/(1.e-2)**0.5,"-v",markersize=6,linewidth=3.0,color="red",label=r"$10^{-2}$")

####矢印の描き方#####
#plt.annotate("",xy=(終点のx, 終点のy), xytext=(始点のx, 始点のy),arrowprops=dict(edgecolor=矢印の枠線の色,facecolor=矢印の塗りつぶしの色, shrink=0.05,linewidth=線の太さ))

plt.annotate("",xy=(1.66936679363601e-01, 1.e-7), xytext=(1.66936679363601e-01, 1.e-6),arrowprops=dict(edgecolor='black',facecolor='black', shrink=0.05,linewidth=0.5))
ax1.text(3.e-2,2.e-6, r"$\gamma_{\mathrm{s}}/\delta\varphi$",size=40,color="black")

plt.xlim(3.e-8,3.e+5)
plt.ylim(1.e-7,1.e+2)
plt.xticks(color='k', size=42)
plt.yticks(color='k', size=42) #軸の書式
plt.xlabel(r"$$\gamma/\delta\varphi$$",color='k', size=42)
plt.ylabel(r"$\mu(\gamma)/\delta\varphi^{1/2}$",color='k', size=42) #軸ラベル

#目盛設定
plt.tick_params(which='major',width = 1.5, length = 10, direction="in",pad=10)
plt.tick_params(which='minor',width = 1.5, length = 5, direction="in",pad=10)
ax1.spines['top'].set_linewidth(2.5)
ax1.spines['bottom'].set_linewidth(2.5)
ax1.spines['left'].set_linewidth(2.5)
ax1.spines['right'].set_linewidth(2.5)
leg=plt.legend(ncol=1, loc=4, borderaxespad=0.35, fontsize=35,frameon=True,edgecolor="black",handletextpad=0.2,handlelength=1) #凡例の書式 locで位置指定/Trueで囲みをつける, Falseで囲みなし
leg.get_frame().set_linewidth(2.5)
for handle in leg.legend_handles:
    handle.set_markersize(6)


plt.savefig('./shear_mu_dp0.000100.pdf',bbox_inches="tight") #保存
plt.show() #下にプロット結果を出力
