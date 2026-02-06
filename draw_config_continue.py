%matplotlib inline
import math
import matplotlib
#matplotlib.use("Agg")
import matplotlib.cm as cm  # colormap
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from scipy.interpolate import Rbf

plt.rcParams['font.family'] = 'Arial' #使用するフォント名
plt.rcParams["text.usetex"] =True
plt.rcParams["font.size"] = 25

from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle
import numpy as np
import math

resolution = 50 # the number of vertices

fig = plt.figure(figsize=(14,10))
ax = fig.add_subplot(111)

temp_min = 0.50
num_temp = 3

temp = 0.44
tcl = 7
cnt = 10
seed = 0

types,x,y,z,drp,drt = np.loadtxt("./global_BOTAN_BB/inherent_thermal/Tmin{:.2f}_{:d}/T{:.2f}/T{:.2f}_{:d}_tc{:d}_pred_{:d}.dat".format(temp_min,num_temp,temp,temp,cnt,tcl,seed+1),comments='!', unpack=True, skiprows=1)
#.format(temp_min,num_temp,temp,temp,cnt,tcl,seed+1)でファイル名に入る数字を指定できる

Np = 4096
rho = 1.2
L = (Np/rho)**(1.0/3.0)

xi = np.linspace(0,L, 100)
yi = np.linspace(0,L, 100)
xx, yy = np.meshgrid(xi, yi)

X=[]
Y=[]
dRp=[]
dRt = []

for i in range(Np):
    if 11.1<z[i]<11.9:
        X.append(x[i])
        Y.append(y[i])
        dRp.append(drp[i])
        dRt.append(drt[i])


#粒子変位を連続的に図示する．(補完することで，表示できる)
rbf_t = Rbf(X,Y,dRp, function='thin_plate')
zz_t = rbf_t(xx, yy)
plt.scatter(xx, yy, s=50, c=zz_t, cmap='seismic_r',vmin=0.2,vmax=1)

plt.xlim(0, L)
plt.ylim(0, L)    

plt.colorbar().set_label(r"$C_{\mathrm{B}}(t=t_{\mathrm{B}}/3)$",size=30)

ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.tick_params(which='major',width = 1, length = 10)
plt.tick_params(which='minor',width = 1, length = 5)
plt.xticks([0, 2, 4, 6, 8, 10, 12, 14], color='k', size=30)
plt.yticks([0, 2, 4, 6, 8, 10, 12, 14], color='k', size=30)
plt.xlabel(r"$x/\sigma_{\mathrm{AA}}$",color='k', size=30)
plt.ylabel(r"$y/\sigma_{\mathrm{AA}}$",color='k', size=30)


ax.set_aspect('equal')

plt.savefig('./global_BOTAN_BB/inherent_thermal/Tmin{:.2f}_{:d}/T{:.2f}/CB_pred_T{:.2f}_tc{:d}_{:d}_{:d}.pdf'.format(temp_min,num_temp,temp,temp,cnt,tcl,seed+1),bbox_inches="tight")
plt.show()
