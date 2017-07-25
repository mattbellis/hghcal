from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pylab as plt
import matplotlib.cm as cm


import ROOT

import sys
sys.path.append("./")

from test.scatter_density_artist.py import ScatterDensityArtist
infile = sys.argv[1]

f = ROOT.TFile(infile)

t = f.Get("ana/hgc")

nentries = t.GetEntries()
layers = []
wafers = []
cells = []
x = []
y = []
rz = []

rece = []


t.GetEntry(0)

layer = t.rechit_layer
wafer = t.rechit_wafer
rx = t.rechit_x
ry = t.rechit_y
rz = t.rechit_z
cell = t.rechit_cell
rechit_energy = t.rechit_energy
        
rece += rechit_energy
layers += layer
wafers += wafer
cells += cell
x += rx
y += ry
z += rz

cm1 = plt.get_cmap("RdYlGn")
col = [cm1(rece[i]*10) for i in range(len(rece))]

m = cm.ScalarMappable(cmap=cm.jet)
m.set_array(rece)

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111, projection='scatter_density')
#p = ax.scatter(x,y,z,c=col,s=0.1)
a = ScatterDensityArtist(ax, x, y, z)
ax.add_artist(a)

#plt.colorbar(m)


plt.show()
