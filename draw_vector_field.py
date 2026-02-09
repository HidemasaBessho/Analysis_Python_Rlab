import math
import matplotlib
import matplotlib.cm as cm  # colormap
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle

plt.rcParams['font.family'] = 'Arial' #使用するフォント名
plt.rcParams["text.usetex"] =True
plt.rcParams["font.size"] = 25

resolution = 50 # the number of vertices

fig = plt.figure(figsize=(14,10))
ax = fig.add_subplot(111)


x0,y0,a0 = np.loadtxt("./pm0.9_SS/phi1.2/g1e-6/coord_N16384_cnt0_0.dat",comments='!', unpack=True)
x,y,a = np.loadtxt("./pm0.9_SS/phi1.2/g1e-6/coord_N16384_cnt30_0.dat",comments='!', unpack=True)

Np = 16384
phi = 1.2
gamma_init = 0.003730987754717678
gamma0 = 1.e-6
gamma = gamma_init+gamma0
Nn = 1000
a1 = 1.0
a2 = 1.4
L = np.sqrt(math.pi*Np*(a1*a1+a2*a2)/8.0/phi)

dX = []
dY = []
dR = []
Theta = []

list_nn = [[0] * Nn for i in range(Np)]

def list_verlet(list_nn,x,y,L,gamma,Np,Nn):
    thresh=2.2
    for i in range(Np):
        for j in range(Nn):
            list_nn[i][j]=0
            
    for i in range(Np):
        for j in range(Np):
            if j != i:
                dx = x[j]-x[i]
                dy = y[j]-y[i]
                dy_temp = dy
                dy-=L*math.floor((dy+0.5*L)/L)
                dx-=gamma*L*math.floor((dy_temp+0.5*L)/L)
                dx-=L*math.floor((dx+0.5*L)/L)
                dr2=dx*dx+dy*dy
                if dr2<thresh*thresh:
                    list_nn[i][0] += 1
                    list_nn[i][list_nn[i][0]]=j

list_verlet(list_nn,x,y,L,gamma,Np,Nn)

def calc_affine_force(x,y,a,L,gamma,list_nn,Np,dX,dY,Theta):
    Xixy = [[0] * 2 for i in range(Np)]
    count = 0
    for i in range(Np):
        for j in range(1,list_nn[i][0]+1):
            dx = x[list_nn[i][j]]-x[i]
            dy = y[list_nn[i][j]]-y[i]
            dy_temp = dy
            dy-=L*math.floor((dy+0.5*L)/L)
            dx-=gamma*L*math.floor((dy_temp+0.5*L)/L)
            dx-=L*floor((dx+0.5*L)/L)
            dr = np.sqrt(dx*dx + dy*dy)
            aij = 0.5*(a[i]+a[list_nn[i][j]])
            if dr<aij:
                tij = -(1.0 - (dr/aij))/aij
                kij = 1.0/aij/aij
                nij_x = dx/dr
                nij_y = dy/dr
                Xixy[i][0] += -(kij*dr-tij)*nij_x*nij_y*nij_x/L/L
                Xixy[i][1] += -(kij*dr-tij)*nij_x*nij_y*nij_y/L/L
            else:
                continue
        dX.append(Xixy[i][0])
        dY.append(Xixy[i][1])
        Xi = np.sqrt(Xixy[i][0]*Xixy[i][0]+Xixy[i][1]*Xixy[i][1])
        if Xi==0:
            count += 1
        theta = math.acos(Xixy[i][0]/Xi)
        if Xixy[i][1]<0:
            theta = 2*math.pi-theta
        Theta.append(theta)
    print(count)

calc_affine_force(x,y,a,L,gamma,list_nn,Np,dX,dY,Theta)


dX = np.array(dX)
dY = np.array(dY)
Theta = np.array(Theta)

patches = []

px=[]
py=[]
vx=[]
vy=[]
colors=[]

for i in range(Np):
    px.append(x[i]) #始点のx
    py.append(y[i]) #始点のy
    vx.append(dX[i]*1.e+5) #x成分の方向
    vy.append(dY[i]*1.e+5) #y成分の方向
    colors.append(Theta[i]) #色

im = plt.quiver(px,py,vx,vy,colors,cmap='hsv', scale = 1,scale_units='xy',zorder=100)

cbar =fig.colorbar(im)
im.set_clim(0,2*math.pi)

cbar.set_label(r"$\theta_j$", fontname="Arial", fontsize=30)

#0, \pi, 2\piだけに目盛りが表示されるようにする
tick_locs = [0, np.pi, 2*math.pi]
cbar.set_ticks(tick_locs)
cbar.set_ticklabels([r"$0$", r"$\pi$", r"$2\pi$"])

    
plt.xlim(0, L+gamma*L)
plt.ylim(0, L)


ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.tick_params(which='major',width = 1, length = 10)
plt.tick_params(which='minor',width = 1, length = 5)
plt.xticks(color='k', size=30)
plt.yticks(color='k', size=30)
plt.xlabel(r"$x/\sigma_{\mathrm{S}}$",color='k', size=30)
plt.ylabel(r"$y/\sigma_{\mathrm{S}}$",color='k', size=30)


ax.set_aspect('equal')

plt.show()
