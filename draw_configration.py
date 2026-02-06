%matplotlib inline
import math
import matplotlib
#matplotlib.use("Agg")
import matplotlib.cm as cm  # colormap
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from scipy.interpolate import Rbf
import statistics

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


x,y,a = np.loadtxt("./pm0.9_SS/phi1.2/g1e-2/coord_N16384_cnt37_0.dat",comments='!', unpack=True)

Np = 16384
phi = 1.2
L = np.sqrt(math.pi*(1.0*1.0+1.4*1.4)*Np/8./phi)
gamma = 1.e-2


patches = []

for i in range(Np):
    circle = mpatches.Ellipse((x[i],y[i]), a[i], a[i]) #(x[i],y[i])の位置に長軸=a[i], 短軸=a[i]の楕円
    patches.append(circle) #上記楕円をpatchesに追加する


plt.xlim(0, L+gamma*L)
plt.ylim(0, L)

colors = a #楕円の色 (ここでは粒径a)
p = PatchCollection(patches, cmap="jet", alpha=0.8,ec="black",lw=0) #patches内の楕円を描画, カラーバーはjet, alpha: 透明度, ec: 楕円の枠線の色, lw: 枠線の太さ
p.set_array(colors)
p.set_clim(0.9,1.5) #カラーバーの範囲
ax.add_collection(p)

plt.colorbar(p).set_label(r"$\sigma_j$",size=30) #カラーバーを描画し，ラベルを設定

ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.tick_params(which='major',width = 1, length = 10)
plt.tick_params(which='minor',width = 1, length = 5)
plt.xticks([0,20,40,60,80,100,120],color='k', size=30)
plt.yticks([0,20,40,60,80,100,120],color='k', size=30)
plt.xlabel(r"$x/\sigma_{\mathrm{S}}$",color='k', size=30)
plt.ylabel(r"$y/\sigma_{\mathrm{S}}$",color='k', size=30)


ax.set_aspect('equal')

plt.savefig('./pm0.9_SS/phi1.2/g1e-2/config_phi1.2_g1em2_0.pdf',bbox_inches="tight")
plt.show()
