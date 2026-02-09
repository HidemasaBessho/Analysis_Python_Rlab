%config InlineBackend.figure_format = 'retina'
%matplotlib inline
import matplotlib
import math
from pylab import * #insetを描くのに必要

import matplotlib.cm as cm  # colormap
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
plt.rcParams["font.size"] = 20

plt.rcParams['font.family'] = 'Arial' #使用するフォント名
plt.rcParams["text.usetex"] =True
plt.rc('text', usetex=True)

fig = plt.figure(figsize=(12,8)) ##サイズ指定##

ax1 = fig.add_subplot(111)
plt.xscale('log')
plt.yscale('log')
plt.minorticks_on()

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-5/g1e-6/Time_stress_dp0.00001_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax1.plot(t,txy/1.e-6,"-o",markersize=10,linewidth=4.0,color="blue",label=r"$\delta\varphi=10^{-5}$")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-4/g1e-6/Time_stress_dp0.00010_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax1.plot(t,txy/1.e-6,"-^",markersize=10,linewidth=4.0,color="green",label=r"$10^{-4}$")

t,txy,txye,P,U,f,z,dr=np.loadtxt("./pm0.9_SS/dp1e-3/g1e-6/Time_stress_dp0.00100_g0.0000010.dat", comments='!', unpack=True,skiprows=1)
ax1.plot(t,txy/1.e-6,"-s",markersize=10,linewidth=4.0,color="red",label=r"$10^{-3}$")


plt.xlim(3.e-2,3.e+6)
plt.ylim(1.e-3,0.3)
plt.xticks([1.e+0,1.e+2,1.e+4,1.e+6],color='k', size=45)
plt.yticks(color='k', size=45) #軸の書式
plt.xlabel(r"$$t$$",color='k', size=45)
plt.ylabel(r"$G(t)$",color='k', size=45) #軸ラベル

#目盛設定
ax1.tick_params(axis='x',which='major',width = 2, length = 12.5,direction='in',pad=10)
ax1.tick_params(axis='x',which='minor',width = 2, length = 5,direction='in')
ax1.tick_params(axis='y',which='major',width = 2, length = 12.5,direction='in',pad=10)
ax1.tick_params(axis='y',which='minor',width = 2, length = 5,direction='in')
ax1.spines['top'].set_linewidth(3)
ax1.spines['bottom'].set_linewidth(3)
ax1.spines['left'].set_linewidth(3)
ax1.spines['right'].set_linewidth(3)
leg = plt.legend(loc='lower center', bbox_to_anchor=(0.2,0), ncol=1, fontsize=35, edgecolor="black",handletextpad=0.5,handlelength=1)
leg.get_frame().set_linewidth(3)
for line in leg.get_lines():
    line.set_linewidth(4)
for handle in leg.legend_handles:
    handle.set_markersize(10)
##



#ax1に関連する挿入図
ax1s = axes([0.56, 0.55, 0.32, 0.32]) #図全体における位置と大きさを調整 axes([左の位置, 下の位置, x方向の長さ (図の大きさに対する値), y方向の長さ (図の大きさに対する値)])

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

ax1s.text(1.e+2,0.2, r"$\propto t^{-1/2}$",size=35)

plt.xlim(3.e-2,1.e+5)
plt.ylim(3.e-3,2)
plt.xticks([1.e+0,1.e+2,1.e+4],color='k', size=35)
plt.yticks([1.e-2,1.e-1,1.e+0],color='k', size=35) #軸の書式
plt.xlabel(r"$$t$$",color='k', size=35)
plt.ylabel(r"$f_G(t)$",color='k', size=35) #軸ラベル

#目盛設定
plt.tick_params(which='major',width = 1, length = 10 ,direction='in',pad=7)
plt.tick_params(which='minor',width = 1, length = 0,direction='in')
ax1s.spines['top'].set_linewidth(2)
ax1s.spines['bottom'].set_linewidth(2)
ax1s.spines['left'].set_linewidth(2)
ax1s.spines['right'].set_linewidth(2)


plt.savefig('./pm0.9_SS/linear_stress_relaxation.pdf',bbox_inches="tight") #保存
plt.show() #下にプロット結果を出力
