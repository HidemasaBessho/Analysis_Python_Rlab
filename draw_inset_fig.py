%config InlineBackend.figure_format = 'retina'
%matplotlib inline
import matplotlib
import math
from pylab import * #挿入図のために必要

import matplotlib.cm as cm  # colormap
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
plt.rcParams["font.size"] = 20

plt.rcParams['font.family'] = 'Arial' #使用するフォント名
plt.rcParams["text.usetex"] =True
plt.rc('text', usetex=True)
# Axesを追加
#plt.figure(1)
fig = plt.figure(figsize=(24,16)) ##サイズ指定##

#1番目
ax1 = fig.add_subplot(221)

plt.xscale('log')
plt.yscale('log')
plt.minorticks_on()


t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-5/g1e-6/Time_stress_dp0.00001_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax1.plot(t,txy/1.e-6,"-o",markersize=10,linewidth=4.0,color="blue",label=r"$\delta\varphi=10^{-5}$")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-4/g1e-6/Time_stress_dp0.00010_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax1.plot(t,txy/1.e-6,"-^",markersize=10,linewidth=4.0,color="green",label=r"$10^{-4}$")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-3/g1e-6/Time_stress_dp0.00100_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax1.plot(t,txy/1.e-6,"-s",markersize=10,linewidth=4.0,color="red",label=r"$10^{-3}$")


ax1.text(2.e-4,0.4, r"(a)",size=42)

plt.xlim(3.e-2,3.e+6)
plt.ylim(1.e-3,0.7)
plt.xticks(color='k', size=0)
plt.yticks(color='k', size=45) #軸の書式
plt.ylabel(r"$G(t)$",color='k', size=45) #軸ラベル

#目盛設定
ax1.tick_params(axis='x',which='major',width = 2, length = 12.5,direction='in',pad=10)
ax1.tick_params(axis='x',which='minor',width = 2, length = 5,direction='in')
ax1.tick_params(axis='y',which='major',width = 2, length = 12.5,direction='in',pad=10)
ax1.tick_params(axis='y',which='minor',width = 2, length = 5,direction='in')
# ax1.xaxis.set_visible(False)
ax1.spines['top'].set_linewidth(3)
ax1.spines['bottom'].set_linewidth(3)
ax1.spines['left'].set_linewidth(3)
ax1.spines['right'].set_linewidth(3)
leg = plt.legend(loc='lower center', bbox_to_anchor=(1.,1.01), ncol=3, fontsize=45, edgecolor="black")
leg.get_frame().set_linewidth(3)
for line in leg.get_lines():
    line.set_linewidth(7)
for handle in leg.legend_handles:
    handle.set_markersize(14) #凡例中のマーカーサイズを調整
##

#ax1に関連する挿入図
ax1s = axes([0.295, 0.715, 0.16, 0.16]) #図全体における位置と大きさを調整 axes([左の位置, 下の位置, x方向の長さ (図の大きさに対する値), y方向の長さ (図の大きさに対する値)])

plt.xscale('log')
plt.yscale('log')

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-5/g1e-6/Time_stress_dp0.00001_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax1s.plot(t,(txy-txy[len(txy)-1])/(txy[0]-txy[len(txy)-1]),"-o",markersize=5,linewidth=2.0,color="blue")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-4/g1e-6/Time_stress_dp0.00010_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax1s.plot(t,(txy-txy[len(txy)-1])/(txy[0]-txy[len(txy)-1]),"-^",markersize=5,linewidth=2.0,color="green")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-3/g1e-6/Time_stress_dp0.00100_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax1s.plot(t,(txy-txy[len(txy)-1])/(txy[0]-txy[len(txy)-1]),"-s",markersize=5,linewidth=2.0,color="red")


x = np.linspace(-1,5,1000)
y = 1.2*(10.0**x)**(-0.5)
ax1s.plot(10.0**x, y, ls = "--",color = "black",lw=3,label=r"slope$=-0.5$")

ax1s.text(1.e+2,0.2, r"$\propto t^{-1/2}$",size=40)

plt.xlim(3.e-2,1.e+5)
plt.ylim(3.e-3,2)
plt.xticks([1.e+0,1.e+2,1.e+4],color='k', size=40)
plt.yticks([1.e-2,1.e-1,1.e+0],color='k', size=40) #軸の書式
plt.xlabel(r"$$t$$",color='k', size=40)
plt.ylabel(r"$f_G(t)$",color='k', size=40) #軸ラベル

#目盛設定
plt.tick_params(which='major',width = 1, length = 10 ,direction='in',pad=7)
plt.tick_params(which='minor',width = 1, length = 0,direction='in')
ax1s.spines['top'].set_linewidth(2)
ax1s.spines['bottom'].set_linewidth(2)
ax1s.spines['left'].set_linewidth(2)
ax1s.spines['right'].set_linewidth(2)

######


#2番目
ax2 = fig.add_subplot(222)
plt.xscale('log')
plt.yscale('log')

Np = 1156


t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-5/g1e-6/Time_stress_dp0.00001_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax2.plot(t,U-1.875795640526871e-11,"-o",markersize=10,linewidth=4.0,color="blue")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-4/g1e-6/Time_stress_dp0.00010_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax2.plot(t,U-0.0000000020896113,"-^",markersize=10,linewidth=4.0,color="green")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-3/g1e-6/Time_stress_dp0.00100_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax2.plot(t,U-2.147368678548506e-07,"-s",markersize=10,linewidth=4.0,color="red",label=r"$\delta\varphi=10^{-3}$")


ax2.text(2.e-4,2.4e-13, r"(b)",size=45)

plt.xlim(3.e-2,3.e+6)
plt.ylim(9.e-16,4.e-13)
plt.xticks([1.e+0,1.e+2,1.e+4,1.e+6],color='k', size=0)
plt.yticks(color='k', size=45) #軸の書式
plt.ylabel(r"$E(t)$",color='k', size=45) #軸ラベル

#目盛設定
plt.tick_params(axis='x',which='major',width = 2, length = 12.5,direction='in',pad=10)
plt.tick_params(axis='x',which='minor',width = 2, length = 5,direction='in')
plt.tick_params(axis='y',which='major',width = 2, length = 12.5,direction='in',pad=10)
plt.tick_params(axis='y',which='minor',width = 2, length = 5,direction='in')
ax2.spines['top'].set_linewidth(3)
ax2.spines['bottom'].set_linewidth(3)
ax2.spines['left'].set_linewidth(3)
ax2.spines['right'].set_linewidth(3)



ax2s = axes([0.735, 0.715, 0.16, 0.16])

plt.xscale('log')
plt.yscale('log')

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-5/g1e-6/Time_stress_dp0.00001_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax2s.plot(t,(U-U[len(U)-1])/(U[0]-U[len(U)-1]),"-o",markersize=5,linewidth=2.0,color="blue")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-4/g1e-6/Time_stress_dp0.00010_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax2s.plot(t,(U-U[len(U)-1])/(U[0]-U[len(U)-1]),"-^",markersize=5,linewidth=2.0,color="green")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-3/g1e-6/Time_stress_dp0.00100_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax2s.plot(t,(U-U[len(U)-1])/(U[0]-U[len(U)-1]),"-s",markersize=5,linewidth=2.0,color="red")


x = np.linspace(-1,5,1000)
y = 0.8*(10.0**x)**(-0.5)
ax2s.plot(10.0**x, y, ls = "--",color = "black",lw=3,label=r"slope$=-0.5$")

ax2s.text(1.e+2,0.2, r"$\propto t^{-1/2}$",size=40)

plt.xlim(3.e-2,1.e+5)
plt.ylim(3.e-3,2)
plt.xticks([1.e+0,1.e+2,1.e+4,],color='k', size=40)
plt.yticks([1.e-2,1.e-1,1.e+0],color='k', size=40) #軸の書式
plt.xlabel(r"$$t$$",color='k', size=40)
plt.ylabel(r"$f_E(t)$",color='k', size=40) #軸ラベル

#目盛設定
plt.tick_params(which='major',width = 1, length = 10,direction='in',pad=7)
plt.tick_params(which='minor',width = 1, length = 0,direction='in')
ax2s.spines['top'].set_linewidth(2)
ax2s.spines['bottom'].set_linewidth(2)
ax2s.spines['left'].set_linewidth(2)
ax2s.spines['right'].set_linewidth(2)



#3番目
ax3 = fig.add_subplot(223)
plt.xscale('log')
plt.yscale('log')

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-5/g1e-6/Time_stress_dp0.00001_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax3.plot(t,f,"-o",markersize=10,linewidth=4.0,color="blue")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-4/g1e-6/Time_stress_dp0.00010_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax3.plot(t,f,"-^",markersize=10,linewidth=4.0,color="green")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-3/g1e-6/Time_stress_dp0.00100_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax3.plot(t,f,"-s",markersize=10,linewidth=4.0,color="red")


ax3.text(2.e-4,3.e-7, r"(c)",size=45)

x = np.linspace(-1,7,1000)
y = 1.e-6*0.17*(10.0**x)**(-3/4)
ax3.plot(10.0**x, y, ls = "--",color = "black",lw=3,label=r"slope$=-0.75$")

ax3.text(3.e+2,1.e-8, r"$\propto t^{-3/4}$",size=45)

plt.xlim(3.e-2,3.e+6)
plt.ylim(3.e-13,1.e-6)
# plt.ylim(1.e-5,4.e-1)
plt.xticks([1.e+0,1.e+2,1.e+4,1.e+6],color='k', size=45)
plt.yticks(color='k', size=45) #軸の書式
plt.xlabel(r"$$t$$",color='k', size=45)
plt.ylabel(r"$F(t)$",color='k', size=45) #軸ラベル

#目盛設定
plt.tick_params(which='major',width = 2, length = 12.5,direction='in',pad=10)
plt.tick_params(which='minor',width = 2, length = 5,direction='in')
ax3.spines['top'].set_linewidth(3)
ax3.spines['bottom'].set_linewidth(3)
ax3.spines['left'].set_linewidth(3)
ax3.spines['right'].set_linewidth(3)


#4番目
ax4 = fig.add_subplot(224)
plt.xscale('log')
plt.yscale('log')

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-5/g1e-6/Time_stress_dp0.00001_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax4.plot(t,dr,"-o",markersize=10,linewidth=4.0,color="blue")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-4/g1e-6/Time_stress_dp0.00010_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax4.plot(t,dr,"-^",markersize=10,linewidth=4.0,color="green")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-3/g1e-6/Time_stress_dp0.00100_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax4.plot(t,dr,"-s",markersize=10,linewidth=4.0,color="red")

ax4.text(2.e-4,6.e-6, r"(d)",size=45)

x = np.linspace(-2,7,1000)
y = 3.3e-7*(10.0**x)**(0.25)
ax4.plot(10.0**x, y, ls = "--",color = "black",lw=3,label=r"slope$=0.25$")

ax4.text(3.e+1,2.5e-6, r"$\propto t^{1/4}$",size=45)

plt.xlim(3.e-2,3.e+6)
plt.ylim(1.e-8,1.e-5)
# plt.ylim(1.e-5,3.e-1)
plt.xticks([1.e+0,1.e+2,1.e+4,1.e+6],color='k', size=45)
plt.yticks(color='k', size=45) #軸の書式
plt.xlabel(r"$$t$$",color='k', size=45)
plt.ylabel(r"$\delta r(t)$",color='k', size=45) #軸ラベル
# plt.ylabel(r"$u(t)$",color='k', size=35) #軸ラベル

#目盛設定
plt.tick_params(which='major',width = 2, length = 12.5,direction='in',pad=10)
plt.tick_params(which='minor',width = 2, length = 5,direction='in')
ax4.spines['top'].set_linewidth(3)
ax4.spines['bottom'].set_linewidth(3)
ax4.spines['left'].set_linewidth(3)
ax4.spines['right'].set_linewidth(3)

plt.subplots_adjust(wspace=0.29, hspace=0.08)


plt.savefig('./pm0.9_SS/Fig3_linear_stress_relaxation.pdf',bbox_inches="tight") #保存

plt.show() #下にプロット結果を出力
